import time

from agents.vwap_based import VWAPBasedTradingAgent
from agents.orderbook_observer import OrderBookObserverAgent
from agents.random_buy_agent import RandomBuyTradingAgent
from utils.config import RANDOM_API_KEY, VWAP_API_KEY, ORDERBOOK_API_KEY

def main():
    # Instantiate agents with descriptive strategy names.
    agents = [
        VWAPBasedTradingAgent(name="VWAPStrategyAgent", api_key=VWAP_API_KEY),
        OrderBookObserverAgent(name="OrderBookObserverAgent", api_key=ORDERBOOK_API_KEY),
        RandomBuyTradingAgent(name="RandomBuyStrategyAgent1", api_key=RANDOM_API_KEY),
        RandomBuyTradingAgent(name="RandomBuyStrategyAgent2", api_key=RANDOM_API_KEY)
    ]
    
    while True:
        # Run each agent's strategy
        for agent in agents:
            print(f"Starting agent: {agent.name}")
            agent.run()
            print("------\n")
        time.sleep(10)
if __name__ == "__main__":
    main() 