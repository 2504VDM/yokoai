from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from typing import List, Dict
import logging
from agent.agent import Agent
import asyncio

logger = logging.getLogger(__name__)

# Create your views here.

class ChatView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.agent = Agent()
            logger.info("Agent initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize agent: {str(e)}")
            raise
    
    def post(self, request):
        """Handle chat messages with the agent.
        
        Expected request format:
        {
            "messages": [
                {"role": "user", "content": "What's the weather in San Francisco?"}
            ],
            "thread_id": "optional-thread-id"
        }
        """
        try:
            messages = request.data.get("messages", [])
            thread_id = request.data.get("thread_id", "default")
            
            logger.info(f"Received chat request - Thread ID: {thread_id}")
            
            if not messages:
                logger.warning("No messages provided in request")
                return Response(
                    {"error": "No messages provided"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            logger.debug(f"Processing messages: {messages}")
            # Run the agent.invoke in a thread pool to handle the async operation
            response = asyncio.run(self.agent.invoke(messages, thread_id))
            logger.info("Successfully generated response")
            
            return Response(response)
        except ValueError as e:
            logger.error(f"Validation error: {str(e)}")
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logger.error(f"Error processing chat request: {str(e)}")
            return Response(
                {
                    "error": "Internal server error",
                    "detail": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
