from sala.models import Sala
from rest_framework import serializers
from caso.serializers import CasoSerializer

class ActionSerializer(serializers.Serializer):
    time = serializers.DateTimeField()
    text = serializers.CharField()
