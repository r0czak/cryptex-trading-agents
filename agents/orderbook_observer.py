from agents.base_agent import BaseAgent
from services.order_service import get_buy_orders, get_sell_orders, place_order, get_buy_orders_foreign, get_sell_orders_foreign
from services.finance_service import get_finance_info
from utils.config import ORDERBOOK_API_KEY

# Renamed the class for a more descriptive name.
class OrderBookObserverAgent(BaseAgent):
    def __init__(self, name, api_key):
        super().__init__(name)
        self.api_key = api_key

    def run(self):
        print(f"{self.name}: Running passive market trading strategy.")

        params = {
            "symbol": "BTC",
            "page": 1,
            "size": 1
        }
        
        # Retrieve order book data
        sell_response = get_sell_orders_foreign(self.api_key, params)
        buy_response = get_buy_orders_foreign(self.api_key, params)
        
        best_ask = None
        best_bid = None

        if sell_response.ok:
            if len(sell_response.json().get("content")) > 0:
                best_ask = sell_response.json().get("content")[0].get("price")
                print(f"{self.name}: Best ask price from sell orders: {best_ask}")
            else:
                print(f"{self.name}: No sell orders available.")
        else:
            print(f"{self.name}: Failed to fetch sell orders. Error: {sell_response.text}")

        if buy_response.ok:
            if len(buy_response.json().get("content")) > 0:
                best_bid = buy_response.json().get("content")[0].get("price")
                print(f"{self.name}: Best bid price from buy orders: {best_bid}")
            else:
                print(f"{self.name}: No buy orders available.")
        else:
            print(f"{self.name}: Failed to fetch buy orders. Error: {buy_response.text}")

        # Retrieve wallet IDs from finance info endpoint
        response = get_finance_info(self.api_key)
        if response.ok:
            data = response.json()
            crypto_wallet_id = data.get("cryptoWallets")[0].get("cryptoWalletId")
            fiat_wallet_id = data.get("fiatWallets")[0].get("fiatWalletId")
        else:
            print(f"{self.name}: Cannot trade, wallet information is missing.")
            return

        # Execute buy order if best ask price exists
        if best_ask is not None:
            buy_order_data = {
                "type": "BUY",
                "cryptoSymbol": "BTC",
                "fiatSymbol": "USD",
                "amount": 1,
                "price": best_ask,
                "cryptoWalletId": crypto_wallet_id,
                "fiatWalletId": fiat_wallet_id
            }
            buy_order_response = place_order(buy_order_data, self.api_key)
            if buy_order_response.ok:
                print(f"{self.name}: Buy order placed successfully: {buy_order_response.json()}")
            else:
                print(f"{self.name}: Failed to place buy order. Error: {buy_order_response.text}")
        else:
            print(f"{self.name}: Skipping buy order due to lack of sell order data.")

        # Execute sell order if best bid price exists
        if best_bid is not None:
            sell_order_data = {
                "type": "SELL",
                "cryptoSymbol": "BTC",
                "fiatSymbol": "USD",
                "amount": 1,
                "price": best_bid,
                "cryptoWalletId": crypto_wallet_id,
                "fiatWalletId": fiat_wallet_id
            }
            sell_order_response = place_order(sell_order_data, self.api_key)
            if sell_order_response.ok:
                print(f"{self.name}: Sell order placed successfully: {sell_order_response.json()}")
            else:
                print(f"{self.name}: Failed to place sell order. Error: {sell_order_response.text}")
        else:
            print(f"{self.name}: Skipping sell order due to lack of buy order data.") 