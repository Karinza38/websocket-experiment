from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import GlobalCounterSerializer

from ..models import GlobalCounter


class CounterView(APIView):
    def post(self, request, *args, **kwargs):
        counter = GlobalCounter.get_solo()
        counter.count += 1
        counter.save()
        return Response()

    def get(self, request, *args, **kwargs):
        counter = GlobalCounter.get_solo()
        serializer = GlobalCounterSerializer(instance=counter)
        return Response(serializer.data)
