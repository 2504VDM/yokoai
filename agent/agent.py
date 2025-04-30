from typing import List, Dict, Any
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.runnables import RunnableConfig
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
import json
from agent.character import AGENT_CHARACTER_PROMPT
from agent.conversation_state import ConversationState

# Load environment variables
load_dotenv()

class Agent:
    def __init__(self):
        # Get API key from environment
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        
        # Initialize the LLM
        self.model = init_chat_model(
            "anthropic:claude-3-7-sonnet-latest",
            temperature=0.7,  # Increased for more creative responses
            anthropic_api_key=api_key
        )
        
        # System message to define the agent's personality
        self.system_message = SystemMessage(content=AGENT_CHARACTER_PROMPT)
        # Initialize conversation state
        self.conversation_state = ConversationState()

    def invoke(self, messages: List[Dict[str, str]], thread_id: str = "default") -> Dict[str, Any]:
        """Invoke the agent with a list of messages.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys.
            thread_id: Unique identifier for the conversation thread.
            
        Returns:
            The agent's response.
        """
        print("Received messages:", json.dumps(messages, indent=2))
        print(f"Thread ID: {thread_id}")
        
        # Update conversation state
        self.conversation_state.messages = messages
        self.conversation_state.thread_id = thread_id
        
        # Convert messages to LangChain format
        langchain_messages = [self.system_message]
        for msg in messages:
            print(f"Processing message - Role: {msg['role']}, Content: {msg['content']}")
            if msg["role"] == "user":
                langchain_messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                langchain_messages.append(AIMessage(content=msg["content"]))
        
        print("Converted messages to LangChain format:", langchain_messages)
        
        # Get response from the model
        response = self.model.invoke(langchain_messages)
        print("Model response:", response)
        print("Response content:", response.content)
        
        # Only return the new assistant message
        result = {"content": response.content}
        print("Final response:", json.dumps(result, indent=2))
        return result 