from django.urls import path
from .views import ChatView
from django.urls import re_path
from django.views.decorators.http import require_http_methods

urlpatterns = [
    re_path(r'^chat/$', require_http_methods(["POST"])(ChatView.as_view()), name='chat'),
] 