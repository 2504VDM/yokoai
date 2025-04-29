from typing import Dict, List, Optional
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model
import json

INTENT_CLASSIFICATION_PROMPT = """You are an intent classification system for an AI assistant named Yoko, who takes on the persona of a highly intelligent and helpful border collie.
Your task is to classify the user's message into one of the following intents:

1. greeting - General greetings or conversation starters
2. question - User is asking for information or explanation
3. task_request - User wants Yoko to perform a specific task
4. clarification - User is asking for clarification or more details
5. feedback - User is providing feedback or expressing emotion
6. farewell - User is ending the conversation
7. preference_setting - User is expressing preferences or customization requests
8. general_chat - Casual conversation without specific intent

Analyze the message and return a JSON object with:
- primary_intent: The main intent of the message
- confidence: A float between 0 and 1 indicating confidence in the classification
- entities: Any key entities or topics mentioned
- sentiment: The emotional tone (positive, negative, neutral)

Example response:
{
    "primary_intent": "question",
    "confidence": 0.95,
    "entities": ["weather", "San Francisco"],
    "sentiment": "neutral"
}

User message: """

class IntentClassifier:
    def __init__(self, model_name: str = "anthropic:claude-3-7-sonnet-latest"):
        self.model = init_chat_model(model_name)
        
    async def classify(self, message: str) -> Dict:
        """Classify the intent of a user message."""
        messages = [
            SystemMessage(content=INTENT_CLASSIFICATION_PROMPT),
            HumanMessage(content=message)
        ]
        
        response = await self.model.ainvoke(messages)
        
        try:
            # Parse the JSON response
            classification = json.loads(response.content)
            return classification
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails
            return {
                "primary_intent": "general_chat",
                "confidence": 0.5,
                "entities": [],
                "sentiment": "neutral"
            } 