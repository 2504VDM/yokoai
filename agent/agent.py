from typing import List, Dict, Any
from agent.enhanced_agent import EnhancedAgent

class Agent:
    def __init__(self):
        self.agent = EnhancedAgent()

    def invoke(self, messages: List[Dict[str, str]], thread_id: str = "default") -> Dict[str, Any]:
        """Invoke the agent with a list of messages.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys.
            thread_id: Unique identifier for the conversation thread.
            
        Returns:
            The agent's response.
        """
        return self.agent.invoke(messages, thread_id) 