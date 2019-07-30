from django.urls import include, path
from . import views

urlpatterns = [
    path('all/', views.todas_salas),
    path('create/', views.criar_sala),
    path('exit/', views.sair_sala),
]