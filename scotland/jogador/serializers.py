from django.contrib.auth.models import User
from .models import Jogador
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    email = serializers.EmailField()
    username = serializers.CharField(max_length=200)
    
class JogadorSerializer(serializers.Serializer):
    class Meta:
        model = Jogador
        fields = '__all__'