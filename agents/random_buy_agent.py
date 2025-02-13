import random
from agents.base_agent import BaseAgent
from services.vwap_service import get_current_vwap
from services.order_service import place_order
from services.finance_service import get_finance_info

class RandomBuyTradingAgent(BaseAgent):
    def __init__(self, name, api_key):
        super().__init__(name)
        self.api_key = api_key

    def run(self):
        print(f"{self.name}: Running random buy strategy.")
        response = get_current_vwap(self.api_key)
        if response.ok:
            data = response.json()
            base_price = data.get("vwap")
            if base_price is None:
                print(f"{self.name}: VWAP data not available.")
                return

            # Generate a random deviation in the range [-2500, 2500]
            deviation = abs(round(random.uniform(-2500, 2500), 2))
            order_price = base_price + deviation

            # Retrieve wallet IDs dynamically.
            response = get_finance_info(self.api_key)
            if response.ok:
                data = response.json()
                crypto_wallet_id = data.get("cryptoWallets")[0].get("cryptoWalletId")
                fiat_wallet_id = data.get("fiatWallets")[0].get("fiatWalletId")
            else:
                print(f"{self.name}: Cannot trade, wallet information is missing.")
                return
            
            order_type = random.choice(["BUY", "SELL"])
            amount = round(random.uniform(0.0001, 2), 8)

            # Always placing a buy order with proper JSON payload
            order_data = {
                "type": order_type,
                "cryptoSymbol": "BTC",
                "fiatSymbol": "USD",
                "amount": amount,
                "price": order_price,
                "cryptoWalletId": crypto_wallet_id,
                "fiatWalletId": fiat_wallet_id
            }
            print(f"{self.name}: Placing buy order with base VWAP {base_price} and deviation {deviation:.2f}, order price: {order_price:.2f}")
            order_response = place_order(order_data, self.api_key)
            if order_response.ok:
                print(f"{self.name}: Order placed successfully: {order_response.json()}")
            else:
                print(f"{self.name}: Failed to place order. Error: {order_response.text}")
        else:
            print(f"{self.name}: Failed to fetch current VWAP. Error: {response}") 