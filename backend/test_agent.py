from agent.agent import Agent

def main():
    # Initialize the agent
    agent = Agent()
    
    # Test conversation
    messages = [
        {"role": "user", "content": "What's the weather in San Francisco?"}
    ]
    
    # Get response
    response = agent.invoke(messages)
    print("Agent Response:", response)

if __name__ == "__main__":
    main() 