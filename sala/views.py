from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)
from jogador.models import Jogador
from jogador.serializers import JogadorSerializer
from scotland.settings import SECRET_KEY
import jwt
import requests
from jogador.views import make_jogador
from jogador.models import Jogador
from sala.models import Sala
from sala.serializers import SalaSerializer

@api_view(["GET"])
def todas_salas(request):
    salas = Sala.objects.all()
    serializer = SalaSerializer(salas, many=True)
    return Response(data=serializer.data,status=HTTP_200_OK)

@api_view(["POST"])
def criar_sala(request):
    jwt_token = request.data.get('token')
    #try:
    jogador = make_jogador(jwt_token)
    #except:
     #   return Response({'error':'Usuário não identificado'}, status=HTTP_403_FORBIDDEN)
    salas = Sala.objects.filter(jogadores=0)
    try:
        sala = salas[0]
    except IndexError:
        sala = Sala()
    jogador.sala_id = sala.id
    jogador.save()
    sala.jogadores = len(Jogador.objects.filter(sala_id=sala.id))
    sala.save()
    
    serializer = JogadorSerializer(jogador)
    return Response(data=serializer.data,status=HTTP_200_OK)

    
# Create your views here.
