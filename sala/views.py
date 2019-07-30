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
    try:
        jogador = make_jogador(jwt_token)
    except:
        return Response({'error':'Usuário não identificado'}, status=HTTP_403_FORBIDDEN)
    salas = Sala.objects.filter(jogadores=0)
    try:
        sala = salas[0]
    except IndexError:
        sala = Sala()
    jogador.sala_id = sala.id
    jogador.save()
    update(sala)
    sala.save()
    
    serializer = SalaSerializer(sala)
    return Response(data=serializer.data,status=HTTP_200_OK)

@api_view(["POST"])
def sair_sala(request):
    jwt_token = request.data.get('token')
    try:
        jogador = make_jogador(jwt_token)
    except:
        return Response({'error':'Usuário não identificado'}, status=HTTP_403_FORBIDDEN)
    if(not jogador.sala_id):
        return Response({'error':'Jogador não está em uma sala'}, status=HTTP_400_BAD_REQUEST)

    sala = Sala.objects.get(id=jogador.sala_id)
    jogador.sala_id = ''
    jogador.save()
    update(sala)
    serializer = SalaSerializer(sala)
    return Response(data=serializer.data,status=HTTP_200_OK)

@api_view(["POST"])
def entrar_sala(request):
    jwt_token = request.data.get('token')
    sala_id = request.data.get('id')
    try:
        jogador = make_jogador(jwt_token)
    except:
        return Response({'error':'Usuário não identificado'}, status=HTTP_403_FORBIDDEN)

    try:
        sala = Sala.objects.get(id=sala_id)
    except Sala.DoesNotExist:
        return Response({'error':'A sala não foi encontrada'}, status=HTTP_400_BAD_REQUEST)
    jogador.sala_id = sala.id
    jogador.save()
    update(sala)
    serializer = SalaSerializer(sala)
    return Response(data=serializer.data,status=HTTP_200_OK)

def update(sala):
    sala.jogadores = len(Jogador.objects.filter(sala_id=sala.id))
    sala.save()