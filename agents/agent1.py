from agents.base_agent import BaseAgent
from services.vwap_service import get_current_vwap
from services.order_service import place_order

class ExampleTradingAgent(BaseAgent):
    def run(self):
        print(f"{self.name}: Running trading strategy.")
        response = get_current_vwap()
        if response.ok:
            current_vwap_data = response.json()
            # Assuming the response contains a key "vwap" representing the current price
            price = current_vwap_data.get("vwap")
            if price is None:
                print(f"{self.name}: VWAP data not available.")
                return

            # Simple strategy: buy if price is below 50,000; otherwise, sell.
            order_type = "buy" if price < 50000 else "sell"
            order_data = {
                "type": order_type,
                "symbol": "BTC-USD",
                "amount": 1,
                "price": price
            }
            order_response = place_order(order_data)
            if order_response.ok:
                print(f"{self.name}: Order placed successfully: {order_response.json()}")
            else:
                print(f"{self.name}: Failed to place order. Error: {order_response.text}")
        else:
            print(f"{self.name}: Failed to fetch current VWAP. Error: {response.text}") 