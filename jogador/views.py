from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)
from django.contrib.auth.models import User
from .models import Jogador
from .serializers import JogadorSerializer
from scotland.settings import SECRET_KEY
import jwt
import requests

@api_view(["GET"])
def todos_jogadores(request):
    print('aklalalal')
    jogadores = Jogador.objects.all()
    print('jogadores: ', jogadores)
    serializer = JogadorSerializer(jogadores, many=True)
    return Response(data=serializer.data,status=HTTP_200_OK)

@api_view(["POST"])
def get_jogador(request):
    jwt_token = request.data.get('token')
    try:
        jogador = make_jogador(jwt_token)
    except:
        return Response({'error':'Usuário não identificado'}, status=HTTP_403_FORBIDDEN)
    serializer = JogadorSerializer(jogador)
    return Response(data=serializer.data,status=HTTP_200_OK)

@api_view(["POST"])
def reset_jogador(request):
    jwt_token = request.data.get('token')
    try:
        jogador = make_jogador(jwt_token)
    except:
        return Response({'error':'Usuário não identificado'}, status=HTTP_403_FORBIDDEN)
    jogador.pista_banco=False
    jogador.pista_bar=False
    jogador.pista_penhores=False
    jogador.pista_charutaria=False
    jogador.pista_chaveiro=False
    jogador.pista_docas=False
    jogador.pista_carruagens=False
    jogador.pista_farmacia=False
    jogador.pista_hotel=False
    jogador.pista_livraria=False
    jogador.pista_museu=False
    jogador.pista_parque=False
    jogador.pista_syard=False
    jogador.pista_teatro=False
    jogador.save()
    serializer = JogadorSerializer(jogador)
    return Response(data=serializer.data,status=HTTP_200_OK)

@api_view(["POST"])
def update_jogador(request):
    jwt_token = request.data.get('token')
    name = request.data.get('name')
    pista_banco = request.data.get('pista_banco')
    pista_bar = request.data.get('pista_bar')
    pista_penhores = request.data.get('pista_penhores')
    pista_charutaria = request.data.get('pista_charutaria')
    pista_chaveiro = request.data.get('pista_chaveiro')
    pista_docas = request.data.get('pista_docas')
    pista_carruagens = request.data.get('pista_carruagens')
    pista_farmacia = request.data.get('pista_farmacia')
    pista_hotel = request.data.get('pista_hotel')
    pista_livraria = request.data.get('pista_livraria')
    pista_museu = request.data.get('pista_museu')
    pista_parque = request.data.get('pista_parque')
    pista_syard = request.data.get('pista_syard')
    pista_teatro = request.data.get('pista_teatro')
    try:
        jogador = make_jogador(jwt_token)
    except:
        return Response({'error':'Usuário não identificado'}, status=HTTP_403_FORBIDDEN)

    if(name):
        jogador.name=name
    if(pista_banco):
        jogador.pista_banco=pista_banco
    if(pista_bar):
        jogador.pista_bar=pista_bar
    if(pista_penhores):
        jogador.pista_penhores=pista_penhores
    if(pista_charutaria):
        jogador.pista_charutaria=pista_charutaria
    if(pista_chaveiro):
        jogador.pista_chaveiro=pista_chaveiro
    if(pista_docas):
        jogador.pista_docas=pista_docas
    if(pista_carruagens):
        jogador.pista_carruagens=pista_carruagens
    if(pista_farmacia):
        jogador.pista_farmacia=pista_farmacia
    if(pista_hotel):
        jogador.pista_hotel=pista_hotel
    if(pista_livraria):
        jogador.pista_livraria=pista_livraria
    if(pista_museu):
        jogador.pista_museu=pista_museu
    if(pista_parque):
        jogador.pista_parque=pista_parque
    if(pista_syard):
        jogador.pista_syard=pista_syard
    if(pista_teatro):
        jogador.pista_teatro=pista_teatro
    jogador.save()
    serializer = JogadorSerializer(jogador)
    return Response(data=serializer.data,status=HTTP_200_OK)

def make_jogador(jwt_token):
    try:
        user_json = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
        username = user_json['username']
        user = User.objects.get(username = username)
        jogador = Jogador.objects.get(user=user)
        return jogador
    except Jogador.DoesNotExist:
        jogador = Jogador(user=user)
        return jogador
# Create your views here.
