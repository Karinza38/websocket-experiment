from rest_framework import serializers

from ..models import GlobalCounter


class GlobalCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalCounter
        fields = ("count",)
