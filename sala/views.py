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
from caso.models import Caso

@api_view(["GET"])
def todas_salas(request):
    salas = Sala.objects.all()
    serializer = SalaSerializer(salas, many=True)
    return Response(data=serializer.data,status=HTTP_200_OK)

@api_view(["POST"])
def criar_sala(request):
    jwt_token = request.data.get('token')
    caso_id = request.data.get('case_id')
    try:
        jogador = make_jogador(jwt_token)
    except:
        return Response({'error':'Usuário não identificado'}, status=HTTP_403_FORBIDDEN)
    salas = Sala.objects.filter(jogadores=0)
    try:
        sala = salas[0]
    except IndexError:
        sala = Sala()
    if(not caso_id):
        return Response({'error':'Nenhum caso selecionado'}, status=HTTP_400_BAD_REQUEST)
    jogador.sala_id = sala.id
    jogador.save()
    sala.caso_id = caso_id
    sala.save()
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

@api_view(["POST"])
def jogadores_sala(request):
    sala_id = request.data.get('id')
    jogadores = Jogador.objects.filter(sala_id=sala.id)
    serializer = JogadorSerializer(jogadores, many=True)
    return Response(data=serializer.data,status=HTTP_200_OK)
    
@api_view(["POST"])
def jogadores_local(request):
    local = request.data.get('local').lower()
    sala_id = request.data.get('id')
    try:
        sala = Sala.objects.get(id=sala_id)
    except Sala.DoesNotExist:
        return Response({'error':'A sala não foi encontrada'}, status=HTTP_400_BAD_REQUEST)
    if(local=='banco'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_banco=True)
    elif(local=='bar'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_bar=True)
    elif(local=='penhores'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_penhores=True)
    elif(local=='charutaria'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_charutaria=True)
    elif(local=='chaveiro'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_chaveiro=True)
    elif(local=='docas'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_docas=True)
    elif(local=='carruagens'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_carruagens=True)
    elif(local=='farmacia'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_farmacia=True)
    elif(local=='hotel'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_hotel=True)
    elif(local=='livraria'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_livraria=True)
    elif(local=='museu'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_museu=True)
    elif(local=='parque'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_parque=True)
    elif(local=='syard'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_syard=True)
    elif(local=='teatro'):
        jogadores = Jogador.objects.filter(sala_id=sala.id, pista_teatro=True)
    else:
        return Response({'error':'Local inválido'}, status=HTTP_400_BAD_REQUEST)
    serializer = JogadorSerializer(jogadores, many=True)
    return Response(data=serializer.data,status=HTTP_200_OK)

def update(sala):
    sala.jogadores = len(Jogador.objects.filter(sala_id=sala.id))
    sala.save()

