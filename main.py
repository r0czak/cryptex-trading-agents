from agents.agent1 import ExampleTradingAgent
from agents.agent2 import PassiveTradingAgent

def main():
    # Instantiate agents – you can add as many as needed.
    agents = [
        ExampleTradingAgent(name="AggressiveAgent"),
        PassiveTradingAgent(name="PassiveAgent")
    ]
    
    # Run each agent's strategy
    for agent in agents:
        print(f"Starting agent: {agent.name}")
        agent.run()
        print("------\n")

if __name__ == "__main__":
    main() 