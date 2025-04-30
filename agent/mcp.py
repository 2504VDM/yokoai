from typing import List, Dict, Any, Optional, Set
from pydantic import BaseModel, Field
from datetime import datetime
import json
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.runnables import RunnableConfig
import re
from enum import Enum

class ConversationState(str, Enum):
    """Defines possible conversation states."""
    INITIAL = "initial"
    ACTIVE = "active"
    WAITING = "waiting"
    COMPLETED = "completed"
    ERROR = "error"

class StateTransitionRule(BaseModel):
    """Defines rules for state transitions."""
    from_state: ConversationState
    to_state: ConversationState
    condition: str  # Python expression to evaluate
    action: Optional[str] = None  # Optional action to take during transition

class ContextWindow(BaseModel):
    """Represents a sliding window of conversation context."""
    messages: List[Dict[str, str]] = Field(default_factory=list)
    max_size: int = Field(default=10)
    summary: Optional[str] = None
    importance_scores: Dict[int, float] = Field(default_factory=dict)  # Message index -> importance score
    
    def add_message(self, message: Dict[str, str]) -> None:
        """Add a new message to the context window."""
        self.messages.append(message)
        # Calculate importance score for new message
        self.importance_scores[len(self.messages) - 1] = self._calculate_importance(message)
        
        if len(self.messages) > self.max_size:
            self._prune_context()
    
    def _calculate_importance(self, message: Dict[str, str]) -> float:
        """Calculate importance score for a message."""
        score = 1.0  # Base score
        
        # Increase score for user messages
        if message["role"] == "user":
            score *= 1.5
        
        # Increase score for messages with questions
        if "?" in message["content"]:
            score *= 1.2
        
        # Increase score for longer messages
        score *= min(1.0 + (len(message["content"]) / 1000), 2.0)
        
        return score
    
    def _prune_context(self) -> None:
        """Prune the context based on importance scores."""
        # Sort messages by importance score
        sorted_indices = sorted(
            self.importance_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        # Keep the most important messages
        keep_indices = set(idx for idx, _ in sorted_indices[:self.max_size])
        
        # Update messages and scores
        self.messages = [msg for i, msg in enumerate(self.messages) if i in keep_indices]
        self.importance_scores = {i: score for i, (idx, score) in enumerate(sorted_indices[:self.max_size])}
        
        # Update summary
        self.update_summary()
    
    def update_summary(self) -> None:
        """Update the summary of older messages."""
        if len(self.messages) > self.max_size:
            # Create a summary of the most important messages
            important_messages = [
                msg for i, msg in enumerate(self.messages)
                if self.importance_scores.get(i, 0) > 1.0
            ]
            self.summary = f"Previous conversation context: {len(important_messages)} important messages summarized"

class Memory(BaseModel):
    """Represents long-term memory storage."""
    facts: Dict[str, Any] = Field(default_factory=dict)
    preferences: Dict[str, Any] = Field(default_factory=dict)
    last_accessed: datetime = Field(default_factory=datetime.now)
    relevance_scores: Dict[str, float] = Field(default_factory=dict)  # Fact key -> relevance score
    
    def add_fact(self, key: str, value: Any, relevance: float = 1.0) -> None:
        """Add a fact to memory with relevance score."""
        self.facts[key] = value
        self.relevance_scores[key] = relevance
        self.last_accessed = datetime.now()
    
    def get_fact(self, key: str, default: Any = None) -> Any:
        """Retrieve a fact from memory."""
        self.last_accessed = datetime.now()
        return self.facts.get(key, default)
    
    def get_relevant_facts(self, query: str, threshold: float = 0.5) -> List[Dict[str, Any]]:
        """Get facts relevant to a query."""
        relevant_facts = []
        for key, value in self.facts.items():
            score = self.relevance_scores.get(key, 0)
            if score >= threshold:
                relevant_facts.append({"key": key, "value": value, "relevance": score})
        return sorted(relevant_facts, key=lambda x: x["relevance"], reverse=True)

class ModelContextProtocol(BaseModel):
    """Implements the Model Context Protocol for managing conversation context."""
    context_window: ContextWindow = Field(default_factory=ContextWindow)
    memory: Memory = Field(default_factory=Memory)
    current_state: ConversationState = Field(default=ConversationState.INITIAL)
    system_prompt: str = Field(default="")
    thread_id: str = Field(default="default")
    transition_rules: List[StateTransitionRule] = Field(default_factory=list)
    
    def __init__(self, **data):
        super().__init__(**data)
        # Initialize default transition rules
        self._initialize_transition_rules()
    
    def _initialize_transition_rules(self):
        """Initialize default state transition rules."""
        self.transition_rules = [
            StateTransitionRule(
                from_state=ConversationState.INITIAL,
                to_state=ConversationState.ACTIVE,
                condition="len(self.context_window.messages) > 0",
                action="self.memory.add_fact('conversation_started', True)"
            ),
            StateTransitionRule(
                from_state=ConversationState.ACTIVE,
                to_state=ConversationState.WAITING,
                condition="'?' in message['content']",
                action="self.memory.add_fact('last_question', message['content'])"
            ),
            StateTransitionRule(
                from_state=ConversationState.WAITING,
                to_state=ConversationState.ACTIVE,
                condition="message['role'] == 'assistant'",
                action="self.memory.add_fact('last_answer', message['content'])"
            ),
            StateTransitionRule(
                from_state=ConversationState.ACTIVE,
                to_state=ConversationState.COMPLETED,
                condition="'goodbye' in message['content'].lower()",
                action="self.memory.add_fact('conversation_ended', True)"
            )
        ]
    
    def _evaluate_transition(self, message: Dict[str, str]) -> Optional[ConversationState]:
        """Evaluate if a state transition should occur."""
        for rule in self.transition_rules:
            if rule.from_state == self.current_state:
                try:
                    # Evaluate the condition
                    if eval(rule.condition, {"self": self, "message": message}):
                        # Execute the action if specified
                        if rule.action:
                            exec(rule.action, {"self": self, "message": message})
                        return rule.to_state
                except Exception as e:
                    print(f"Error evaluating transition rule: {e}")
        return None
    
    def process_message(self, message: Dict[str, str]) -> List[Dict[str, str]]:
        """Process a new message and return the full context."""
        # Check for state transition
        new_state = self._evaluate_transition(message)
        if new_state:
            self.current_state = new_state
        
        # Add message to context window
        self.context_window.add_message(message)
        
        # Prepare context for the model
        context = []
        
        # Add system prompt if exists
        if self.system_prompt:
            context.append({"role": "system", "content": self.system_prompt})
        
        # Add current state information
        context.append({
            "role": "system",
            "content": f"Current conversation state: {self.current_state.value}"
        })
        
        # Add summary of older messages if exists
        if self.context_window.summary:
            context.append({"role": "system", "content": self.context_window.summary})
        
        # Add relevant facts from memory
        relevant_facts = self.memory.get_relevant_facts(message["content"])
        if relevant_facts:
            facts_context = "Relevant context from memory:\n" + "\n".join(
                f"- {fact['key']}: {fact['value']}" for fact in relevant_facts
            )
            context.append({"role": "system", "content": facts_context})
        
        # Add current context window
        context.extend(self.context_window.messages)
        
        return context
    
    def update_state(self, new_state: ConversationState) -> None:
        """Update the current state of the conversation."""
        self.current_state = new_state
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the MCP state to a dictionary."""
        return {
            "context_window": {
                "messages": self.context_window.messages,
                "summary": self.context_window.summary,
                "importance_scores": self.context_window.importance_scores
            },
            "memory": {
                "facts": self.memory.facts,
                "preferences": self.memory.preferences,
                "last_accessed": self.memory.last_accessed.isoformat(),
                "relevance_scores": self.memory.relevance_scores
            },
            "current_state": self.current_state.value,
            "system_prompt": self.system_prompt,
            "thread_id": self.thread_id,
            "transition_rules": [rule.dict() for rule in self.transition_rules]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ModelContextProtocol':
        """Create an MCP instance from a dictionary."""
        if isinstance(data.get('memory', {}).get('last_accessed'), str):
            data['memory']['last_accessed'] = datetime.fromisoformat(data['memory']['last_accessed'])
        if isinstance(data.get('current_state'), str):
            data['current_state'] = ConversationState(data['current_state'])
        return cls(**data) 