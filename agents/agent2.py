from agents.base_agent import BaseAgent
from services.order_service import get_buy_orders, get_sell_orders

class PassiveTradingAgent(BaseAgent):
    def run(self):
        print(f"{self.name}: Checking order book.")
        buy_response = get_buy_orders()
        sell_response = get_sell_orders()

        if buy_response.ok:
            buy_orders = buy_response.json()
            print(f"{self.name}: Current buy orders: {buy_orders}")
        else:
            print(f"{self.name}: Failed to fetch buy orders. Error: {buy_response.text}")

        if sell_response.ok:
            sell_orders = sell_response.json()
            print(f"{self.name}: Current sell orders: {sell_orders}")
        else:
            print(f"{self.name}: Failed to fetch sell orders. Error: {sell_response.text}") 