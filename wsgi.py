"""
WSGI config for project.
It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import sys

# Add the project directory to the Python path
current_path = os.path.abspath(os.path.dirname(__file__))
project_path = os.path.dirname(current_path)
if current_path not in sys.path:
    sys.path.append(current_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 