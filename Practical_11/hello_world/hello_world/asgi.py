"""
ASGI config for hello_world project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_world.settings')

application = get_asgi_application()
