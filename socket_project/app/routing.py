from django.urls import path
from . import consumers

print("hello")

websocket_urlpatterns = [
    path('ws/sc/', consumers.MySyncConsumer.as_asgi()),
]
