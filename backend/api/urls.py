# backend/api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('health', views.health_check, name='health_check'),
    path('vandermeulen', views.vandermeulen_data, name='vandermeulen_data'),
    path('test-roi', views.test_roi_analysis, name='test_roi_analysis'),
]