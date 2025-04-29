from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableConfig

class ConversationState(BaseModel):
    """Represents the current state of a conversation."""
    messages: List[Dict[str, str]] = Field(default_factory=list)
    current_intent: Optional[str] = None
    context: Dict[str, Any] = Field(default_factory=dict)
    user_preferences: Dict[str, Any] = Field(default_factory=dict)
    last_updated: datetime = Field(default_factory=datetime.now)
    thread_id: str = Field(default="default")

    def dict(self, *args, **kwargs) -> Dict[str, Any]:
        """Override dict method to ensure all fields are included."""
        return {
            "messages": self.messages,
            "current_intent": self.current_intent,
            "context": self.context,
            "user_preferences": self.user_preferences,
            "last_updated": self.last_updated.isoformat(),
            "thread_id": self.thread_id
        }

class ConversationManager:
    def __init__(self):
        self.graph = self._create_conversation_graph()
        
    def _create_conversation_graph(self) -> StateGraph:
        """Creates the conversation flow graph."""
        # Initialize the graph
        graph = StateGraph(ConversationState)
        
        # Add nodes for different conversation stages
        graph.add_node("intent_classification", self._classify_intent)
        graph.add_node("context_update", self._update_context)
        graph.add_node("response_generation", self._generate_response)
        
        # Define the conversation flow
        graph.set_entry_point("intent_classification")
        graph.add_edge("intent_classification", "context_update")
        graph.add_edge("context_update", "response_generation")
        graph.add_edge("response_generation", END)
        
        return graph.compile()
    
    async def _classify_intent(self, state: Dict) -> Dict:
        """Classifies the user's intent from the latest message."""
        current_state = ConversationState(**state)
        if not current_state.messages:
            return {"current_intent": "greeting"}
            
        latest_message = current_state.messages[-1]["content"]
        # TODO: Implement proper intent classification
        # For now, using a simple placeholder
        intent = "general_query"  # This will be replaced with actual classification
        return {"current_intent": intent}
    
    async def _update_context(self, state: Dict) -> Dict:
        """Updates the conversation context based on the current state."""
        current_state = ConversationState(**state)
        context = current_state.context.copy()
        
        # Update context based on the latest message and intent
        if current_state.current_intent:
            context["last_intent"] = current_state.current_intent
            context["last_update"] = datetime.now().isoformat()
            
        # TODO: Implement more sophisticated context updating
        # This could include:
        # - Entity extraction
        # - Relationship tracking
        # - Topic modeling
        
        return {"context": context}
    
    async def _generate_response(self, state: Dict) -> Dict:
        """Generates a response based on the current state."""
        # Convert dict state back to ConversationState
        current_state = ConversationState(**state)
        return current_state.dict()
    
    async def process_message(self, message: str, thread_id: str = "default") -> Dict[str, Any]:
        """Process a new message through the conversation graph."""
        initial_state = ConversationState(
            messages=[{"role": "user", "content": message}],
            thread_id=thread_id
        )
        
        config = RunnableConfig(
            callbacks=None,  # TODO: Add logging callbacks
        )
        
        # Run the message through the graph
        final_state = await self.graph.ainvoke(initial_state.dict(), config)
        return ConversationState(**final_state).dict() 