from typing import Dict, Any
from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Get weather for a given city.
    
    Args:
        city: The name of the city to get weather for.
        
    Returns:
        A string describing the weather in the city.
    """
    # This is a mock implementation. In a real application, you would
    # call a weather API here.
    return f"It's always sunny in {city}!" 