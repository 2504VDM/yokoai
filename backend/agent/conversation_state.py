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

    def to_dict(self) -> Dict[str, Any]:
        """Convert state to dictionary format."""
        return {
            "messages": self.messages,
            "current_intent": self.current_intent,
            "context": self.context,
            "user_preferences": self.user_preferences,
            "last_updated": self.last_updated.isoformat(),
            "thread_id": self.thread_id
        }

    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from the state by key."""
        return getattr(self, key, default)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ConversationState':
        """Create state from dictionary format."""
        if isinstance(data.get('last_updated'), str):
            data['last_updated'] = datetime.fromisoformat(data['last_updated'])
        return cls(**data) 