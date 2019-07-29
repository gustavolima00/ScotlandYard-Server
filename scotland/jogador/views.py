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
from scotland.settings import *
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
        profile.name=name
        profile.save()

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
