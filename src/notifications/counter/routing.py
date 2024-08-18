from django.urls import path

from .consumers import CounterConsumer

websocket_urlpatterns = [
    path("ws/counter/", CounterConsumer.as_asgi()),
]
