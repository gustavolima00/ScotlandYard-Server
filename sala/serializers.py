from sala.models import Sala
from rest_framework import serializers
from caso.serializers import CasoSerializer

class SalaSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    caso_id = serializers.IntegerField()
    jogadores = serializers.IntegerField()