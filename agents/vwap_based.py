from datetime import datetime, timedelta
from agents.base_agent import BaseAgent
from services.vwap_service import get_current_vwap, get_vwap_history
from services.order_service import place_order
from services.finance_service import get_finance_info

# Renamed the class for a more descriptive name.
class VWAPBasedTradingAgent(BaseAgent):
    def __init__(self, name, api_key):
        super().__init__(name)
        self.api_key = api_key

    def run(self):
        print(f"{self.name}: Running VWAP-based trading strategy.")
        
        # Get current VWAP data with required parameters.
        current_response = get_current_vwap(self.api_key, crypto_symbol="BTC", fiat_symbol="USD", interval="FIVE_MINUTES")
        if not current_response.ok:
            print(f"{self.name}: Failed to fetch current VWAP. Error: {current_response.text}")
            return
        
        current_data = current_response.json()
        price = current_data.get("vwap")
        if price is None:
            print(f"{self.name}: VWAP data not available.")
            return
        
        # Retrieve historical VWAP for the past 1 hour using 5-minute intervals.
        end_date = datetime.now()
        start_date = end_date - timedelta(hours=1)
        history_response = get_vwap_history(
            self.api_key,
            crypto_symbol="BTC", 
            fiat_symbol="USD", 
            start_date=start_date, 
            end_date=end_date, 
            interval="FIVE_MINUTES", 
            page=0, 
            size=12
        )
        if not history_response.ok:
            print(f"{self.name}: Failed to fetch VWAP history. Error: {history_response.text}")
            return
        
        history_data = history_response.json()
        # Check if data is paginated (i.e., has a 'content' field)
        if isinstance(history_data, dict) and "content" in history_data:
            entries = history_data["content"]
        else:
            entries = history_data
        
        if not entries:
            print(f"{self.name}: No VWAP history data available.")
            return
        
        try:
            total = sum(float(entry.get("vwap", 0)) for entry in entries.get("vwapHistory").get("content"))
        except Exception as e:
            print(f"{self.name}: Error computing historical VWAP average: {e}")
            return
        
        historical_avg = total / len(entries)
        print(f"{self.name}: Historical average VWAP (last hour): {historical_avg:.2f}")
        
        # Decide the order type by comparing the current VWAP with the historical average.
        order_type = "BUY" if float(price) < historical_avg else "SELL"
        print(f"{self.name}: Current VWAP is {price:.2f}. Deciding to {order_type} based on historical average.")
        
        # Retrieve dynamic wallet info.
        response = get_finance_info(self.api_key)
        if response.ok:
            data = response.json()
            crypto_wallet_id = data.get("cryptoWallets")[0].get("cryptoWalletId")
            fiat_wallet_id = data.get("fiatWallets")[0].get("fiatWalletId")
        else:
            print(f"{self.name}: Cannot trade, wallet information is missing.")
            return

        order_data = {
            "type": order_type,
            "cryptoSymbol": "BTC",
            "fiatSymbol": "USD",
            "amount": 1,
            "price": price,
            "cryptoWalletId": crypto_wallet_id,
            "fiatWalletId": fiat_wallet_id
        }
        order_response = place_order(order_data, self.api_key)
        if order_response.ok:
            print(f"{self.name}: Order placed successfully: {order_response.json()}")
        else:
            print(f"{self.name}: Failed to place order. Error: {order_response.text}") 