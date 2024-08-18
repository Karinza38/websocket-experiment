import channels.layers
from asgiref.sync import async_to_sync
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from ..models import GlobalCounter
from .serializers import GlobalCounterSerializer


class CounterView(APIView):
    def post(self, request, *args, **kwargs):
        counter = GlobalCounter.get_solo()
        counter.count += 1
        counter.save()

        serializer = GlobalCounterSerializer(instance=counter)
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.group_send)("counter_channel", {"type": "notify", "text": json.dumps(serializer.data)})
        return Response()

    def get(self, request, *args, **kwargs):
        counter = GlobalCounter.get_solo()
        serializer = GlobalCounterSerializer(instance=counter)
        return Response(serializer.data)
