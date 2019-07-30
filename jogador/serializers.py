from django.contrib.auth.models import User
from .models import Jogador
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    email = serializers.EmailField()

class JogadorSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    user = UserSerializer()
    #sala_id = serializers.CharField()
    name = serializers.CharField()
    #pista_banco = serializers.BooleanField()
    #pista_bar = serializers.BooleanField()
    #pista_penhores = serializers.BooleanField()
    #pista_charutaria = serializers.BooleanField()
    #pista_chaveiro = serializers.BooleanField()
    #pista_docas = serializers.BooleanField()
    #pista_carruagens = serializers.BooleanField()
    #pista_farmacia = serializers.BooleanField()
    #pista_hotel = serializers.BooleanField()
    #pista_livraria = serializers.BooleanField()
    #pista_museu = serializers.BooleanField()
    #pista_parque = serializers.BooleanField()
    #pista_syard = serializers.BooleanField()
    #pista_teatro = serializers.BooleanField()