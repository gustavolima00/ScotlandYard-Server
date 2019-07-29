from django.shortcuts import render
from .models import Caso
from rest_framework import viewsets
from .serializers import CasoSerializer

class CasoViewSet(viewsets.ModelViewSet):
    queryset = Caso.objects.all()
    serializer_class = CasoSerializer
# Create your views here.
