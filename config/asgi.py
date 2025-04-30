"""
ASGI config for project.
It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os
import sys
from django.core.asgi import get_asgi_application

# Add the project directory to the Python path
current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if current_path not in sys.path:
    sys.path.append(current_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
