"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import logging
from django.conf import settings
import os
from api.views import landing_page, chat_page

logger = logging.getLogger(__name__)

@require_http_methods(["GET", "HEAD"])
def health_check(request):
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('health/', health_check, name='health_check'),
]

# Add frontend routes only in production
if os.getenv('ENVIRONMENT', 'production') == 'production':
    urlpatterns += [
        path('', landing_page, name='landing_page'),
        path('chat/', chat_page, name='chat_page'),
    ]
else:
    # In staging, show health check at root URL
    urlpatterns += [
        path('', health_check, name='health_check_root'),
    ]
