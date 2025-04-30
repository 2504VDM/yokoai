from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from typing import List, Dict
import logging
from agent.agent import Agent
import asyncio
from concurrent.futures import ThreadPoolExecutor
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import time
import os
from django.http import JsonResponse

logger = logging.getLogger(__name__)

@require_http_methods(["GET"])
def health_check(request):
    """Health check endpoint."""
    try:
        # Test database connection
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        # Log successful health check
        logger.info("Health check passed")
        return JsonResponse({
            "status": "ok",
            "database": "connected",
            "environment": os.getenv('ENVIRONMENT', 'production')
        })
    except Exception as e:
        # Log the error
        logger.error(f"Health check failed: {str(e)}")
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)

@method_decorator(csrf_exempt, name='dispatch')
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
            
            # Run the agent.invoke in a thread pool with timeout
            max_retries = 3
            retry_delay = 2  # seconds
            
            for attempt in range(max_retries):
                try:
                    with ThreadPoolExecutor() as executor:
                        future = executor.submit(self.agent.invoke, messages, thread_id)
                        # Set a timeout for the operation
                        response = future.result(timeout=30)  # 30 second timeout
                    
                    logger.info("Successfully generated response")
                    
                    # Create response with CORS headers
                    response_obj = Response(response)
                    response_obj["Access-Control-Allow-Origin"] = "*"
                    response_obj["Access-Control-Allow-Methods"] = "POST, OPTIONS"
                    response_obj["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
                    response_obj["Access-Control-Max-Age"] = "86400"
                    
                    return response_obj
                    
                except TimeoutError:
                    logger.warning(f"Request timed out (attempt {attempt + 1}/{max_retries})")
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
                        continue
                    raise
                except Exception as e:
                    if "529" in str(e):  # Rate limit error
                        logger.warning(f"Rate limit hit (attempt {attempt + 1}/{max_retries})")
                        if attempt < max_retries - 1:
                            time.sleep(retry_delay * (attempt + 1))  # Exponential backoff
                            continue
                    raise
            
        except ValueError as e:
            logger.error(f"Validation error: {str(e)}")
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except TimeoutError:
            logger.error("Request timed out after all retries")
            return Response(
                {
                    "error": "Request timed out",
                    "detail": "The request took too long to process. Please try again."
                },
                status=status.HTTP_504_GATEWAY_TIMEOUT
            )
        except Exception as e:
            logger.error(f"Error processing chat request: {str(e)}")
            if "529" in str(e):
                return Response(
                    {
                        "error": "Rate limit exceeded",
                        "detail": "The service is currently experiencing high demand. Please try again in a few moments."
                    },
                    status=status.HTTP_429_TOO_MANY_REQUESTS
                )
            return Response(
                {
                    "error": "Internal server error",
                    "detail": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
