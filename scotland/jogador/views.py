from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)
from .models import Jogador
from .serializers import JogadorSerializer

@api_view(["GET"])
def all_profiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(data=serializer.data,status=HTTP_200_OK)

@api_view(["POST"])
def create_player(request):
    jwt_token = request.data.get('token')

# Create your views here.
