from typing import List, Dict, Any
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.runnables import RunnableConfig
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
import json
from agent.character import AGENT_CHARACTER_PROMPT
from agent.conversation_state import ConversationManager
from agent.intent_classifier import IntentClassifier

# Load environment variables
load_dotenv()

class Agent:
    def __init__(self):
        # Get API key from environment
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        
        # Initialize components
        self.model = init_chat_model(
            "anthropic:claude-3-7-sonnet-latest",
            temperature=0.7,  # Increased for more creative responses
            anthropic_api_key=api_key
        )
        
        self.conversation_manager = ConversationManager()
        self.intent_classifier = IntentClassifier()
        
        # System message to define the agent's personality
        self.system_message = SystemMessage(content=AGENT_CHARACTER_PROMPT)

    async def invoke(self, messages: List[Dict[str, str]], thread_id: str = "default") -> Dict[str, Any]:
        """Invoke the agent with a list of messages.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys.
            thread_id: Unique identifier for the conversation thread.
            
        Returns:
            The agent's response.
        """
        print("Received messages:", json.dumps(messages, indent=2))
        print(f"Thread ID: {thread_id}")
        
        # Process the message through the conversation manager
        conversation_state = await self.conversation_manager.process_message(
            messages[-1]["content"],
            thread_id=thread_id
        )
        
        # Convert messages to LangChain format with context
        langchain_messages = [self.system_message]
        
        # Add context from conversation state if available
        if conversation_state.context:
            context_msg = f"\nConversation Context:\n{json.dumps(conversation_state.context, indent=2)}"
            langchain_messages.append(SystemMessage(content=context_msg))
        
        # Add message history
        for msg in messages:
            print(f"Processing message - Role: {msg['role']}, Content: {msg['content']}")
            if msg["role"] == "user":
                langchain_messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                langchain_messages.append(AIMessage(content=msg["content"]))
        
        print("Converted messages to LangChain format:", langchain_messages)
        
        # Get intent classification for the latest message
        intent_data = await self.intent_classifier.classify(messages[-1]["content"])
        print("Intent classification:", intent_data)
        
        # Add intent information to the system context
        intent_context = f"\nCurrent user intent: {intent_data['primary_intent']}\nEntities: {', '.join(intent_data['entities'])}\nSentiment: {intent_data['sentiment']}"
        langchain_messages.append(SystemMessage(content=intent_context))
        
        # Get response from the model
        response = await self.model.ainvoke(langchain_messages)
        print("Model response:", response)
        print("Response content:", response.content)
        
        # Only return the new assistant message
        result = {"content": response.content}
        print("Final response:", json.dumps(result, indent=2))
        return result 