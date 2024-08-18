import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class CounterConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()    
        async_to_sync(self.channel_layer.group_add)("counter_channel", self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("counter_channel", self.channel_name)

    def notify(self, text_data=None):
        self.send(text_data["text"])