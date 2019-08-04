from django.shortcuts import render
from .models import Caso
from rest_framework import viewsets
from .serializers import CasoSerializer
from rest_framework import filters

class CasoViewSet(viewsets.ModelViewSet):
    queryset = Caso.objects.all()
    serializer_class = CasoSerializer
    filter_backends = [filters.SearchFilter]
    #http_method_names = ['get', 'post', 'head', 'put']
    http_method_names = ['get', 'head']
    search_fields = ['titulo']
# Create your views here.
