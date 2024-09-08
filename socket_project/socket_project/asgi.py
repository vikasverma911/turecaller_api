import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path
from app.consumers import MySyncConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socket_project.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        [
            re_path('^ws/sc/', MySyncConsumer.as_asgi()),
        ]
    ),
})
