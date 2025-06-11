from typing import List, Dict, Any, Optional, TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.chat_models import init_chat_model
from langchain_core.runnables import RunnableConfig
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
from datetime import datetime
from agent.mcp import ModelContextProtocol, ConversationState
from agent.character import AGENT_CHARACTER_PROMPT

# Load environment variables
load_dotenv()

class AgentState(TypedDict):
    """Type definition for the agent's state."""
    messages: List[Dict[str, str]]
    current_state: str
    context: Dict[str, Any]
    memory: Dict[str, Any]
    thread_id: str
    error: Optional[str]

class EnhancedAgent:
    def __init__(self):
        # Initialize the LLM
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        
        self.model = init_chat_model(
            "anthropic:claude-3-7-sonnet-latest",
            temperature=0.7,
            anthropic_api_key=api_key
        )
        
        # Initialize MCP
        self.mcp = ModelContextProtocol(
            system_prompt=AGENT_CHARACTER_PROMPT
        )
        
        # Initialize the state graph
        self.graph = self._build_state_graph()
    
    def _build_state_graph(self) -> StateGraph:
        """Build the LangGraph state graph for conversation flow."""
        # Create the graph
        graph = StateGraph(AgentState)
        
        # Define the nodes
        def process_input(state: AgentState) -> AgentState:
            """Process the user input and update state."""
            try:
                # Get the last message
                last_message = state["messages"][-1]
                
                # Process through MCP
                context = self.mcp.process_message(last_message)
                
                # Update state
                state["context"] = self.mcp.to_dict()
                state["current_state"] = self.mcp.current_state.value
                
                return state
            except Exception as e:
                state["error"] = str(e)
                return state
        
        def generate_response(state: AgentState) -> AgentState:
            """Generate a response using the LLM."""
            try:
                # Convert context to LangChain format
                langchain_messages = []
                for msg in state["messages"]:
                    if msg["role"] == "system":
                        langchain_messages.append(SystemMessage(content=msg["content"]))
                    elif msg["role"] == "user":
                        langchain_messages.append(HumanMessage(content=msg["content"]))
                    elif msg["role"] == "assistant":
                        langchain_messages.append(AIMessage(content=msg["content"]))
                
                # Get response from model
                response = self.model.invoke(langchain_messages)
                
                # Add response to messages
                state["messages"].append({
                    "role": "assistant",
                    "content": response.content
                })
                
                return state
            except Exception as e:
                state["error"] = str(e)
                return state
        
        def handle_error(state: AgentState) -> AgentState:
            """Handle any errors that occurred."""
            if state["error"]:
                state["messages"].append({
                    "role": "assistant",
                    "content": f"I apologize, but I encountered an error: {state['error']}. Let's try again!"
                })
                state["error"] = None
            return state
        
        # Add nodes to graph
        graph.add_node("process_input", process_input)
        graph.add_node("generate_response", generate_response)
        graph.add_node("handle_error", handle_error)
        
        # Define edges
        graph.add_edge("process_input", "generate_response")
        graph.add_edge("generate_response", "handle_error")
        graph.add_edge("handle_error", END)
        
        # Set entry point
        graph.set_entry_point("process_input")
        
        return graph.compile()
    
    def invoke(self, messages: List[Dict[str, str]], thread_id: str = "default") -> Dict[str, Any]:
        """Invoke the enhanced agent with a list of messages."""
        # Initialize state
        initial_state: AgentState = {
            "messages": messages,
            "current_state": ConversationState.INITIAL.value,
            "context": {},
            "memory": {},
            "thread_id": thread_id,
            "error": None
        }
        
        # Update MCP thread ID
        self.mcp.thread_id = thread_id
        
        try:
            # Run the graph
            final_state = self.graph.invoke(initial_state)
            
            # Get the last assistant message
            last_assistant_message = next(
                (msg for msg in reversed(final_state["messages"]) 
                 if msg["role"] == "assistant"),
                None
            )
            
            if last_assistant_message:
                return {"content": last_assistant_message["content"]}
            else:
                return {"content": "I apologize, but I couldn't generate a response."}
                
        except Exception as e:
            return {"content": f"I encountered an error: {str(e)}"} 