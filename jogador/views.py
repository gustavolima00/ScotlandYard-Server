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
from sala.models import Sala
from action.models import Action
from .serializers import JogadorSerializer
from scotland.settings import SECRET_KEY
import jwt
import requests

@api_view(["GET"])
def todos_jogadores(request):
    jogadores = Jogador.objects.all()
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
def update_hints(request):
    jwt_token = request.data.get('token')
    places = [
        ('banco', 'Banco'), 
        ('bar', 'Bar'), 
        ('penhores', 'Casa de penhores'), 
        ('charutaria', 'Charutaria'),
        ('chaveiro', 'Chaveiro'),
        ('docas', 'Docas'),
        ('carruagens', 'Estação de carruagens'),
        ('farmacia', 'Farmácia'),
        ('hotel', 'Hotel'),
        ('livraria', 'Livraria'),
        ('museu', 'Museu'),
        ('parque', 'Parque'),
        ('syard', 'Scotland Yard'),
        ('teatro', 'Teatro'),
    ]
    try:
        jogador = make_jogador(jwt_token)
    except:
        return Response({'error':'Usuário não identificado'}, status=HTTP_403_FORBIDDEN)
    try:
        sala = Sala.objects.get(id=jogador.sala_id)
    except Sala.DoesNotExist:
        return Response({'error':'Usuário não está em uma sala'}, status=HTTP_403_FORBIDDEN)
    for place_code, place_name in places:
        hint_place = 'pista_{}'.format(place_code)
        try:
            status = request.data[hint_place]
        except:
            continue        
        print(status)
        if(str(status).lower()=='true'):
            setattr(jogador, hint_place, True)
            action = Action()
            action.text = '{} desbloqueou a pista do(a) {}.'.format(jogador.name, place_name)
            action.room = sala
            action.save()
        else:
            setattr(jogador, hint_place, False)
            action = Action()
            action.text = '{} bloqueou a pista do(a) {}.'.format(jogador.name, place_name)
            action.room = sala
            action.save()
    jogador.save()
    serializer = JogadorSerializer(jogador)
    return Response(data=serializer.data,status=HTTP_200_OK)

@api_view(["POST"])
def update_jogador(request):
    jwt_token = request.data.get('token')
    name = request.data.get('name')
    #try:
    jogador = make_jogador(jwt_token)
    #except:
    #    return Response({'error':'Usuário não identificado'}, status=HTTP_403_FORBIDDEN)
    if(name):
        jogador.name=name
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
