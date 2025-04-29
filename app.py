import os
import sys

# Add the project directory to the Python path
current_path = os.path.abspath(os.path.dirname(__file__))
if current_path not in sys.path:
    sys.path.append(current_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application() 