# backend/config/urls.py
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from api.views import (
    health_check, 
    vdm_payment_widget_data,
    vdm_roi_widget_data, 
    vdm_portfolio_widget_data,
    vdm_dashboard_overview
)

def home_view(request):
    """Simple home page response"""
    return JsonResponse({
        "message": "VDM Nexus API Server",
        "status": "running",
        "version": "1.0.0",
        "endpoints": {
            "admin": "/admin/",
            "health": "/health/",
            "dashboard": "/api/dashboard/vdm/overview/",
            "widgets": {
                "payments": "/api/widgets/vdm/payments/",
                "roi": "/api/widgets/vdm/roi/", 
                "portfolio": "/api/widgets/vdm/portfolio/"
            }
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    
    # Health check
    path('health/', health_check, name='health_check'),
    
    # Widget API endpoints
    path('api/widgets/vdm/payments/', vdm_payment_widget_data, name='vdm_payment_widget'),
    path('api/widgets/vdm/roi/', vdm_roi_widget_data, name='vdm_roi_widget'),
    path('api/widgets/vdm/portfolio/', vdm_portfolio_widget_data, name='vdm_portfolio_widget'),
    path('api/dashboard/vdm/overview/', vdm_dashboard_overview, name='vdm_dashboard_overview'),
]