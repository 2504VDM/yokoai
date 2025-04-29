from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from typing import List, Dict

from agent.agent import Agent

# Create your views here.

class ChatView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.agent = Agent()
    
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
        messages = request.data.get("messages", [])
        thread_id = request.data.get("thread_id", "default")
        
        if not messages:
            return Response(
                {"error": "No messages provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            response = self.agent.invoke(messages, thread_id)
            print('Agent response:', response)
            return Response(response)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
