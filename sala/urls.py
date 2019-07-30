from django.urls import include, path
from sala import views

urlpatterns = [
    path('all/', views.todas_salas),
    path('create/', views.criar_sala),
    path('exit/', views.sair_sala),
    path('join/', views.entrar_sala),
    path('place/', views.jogadores_local),
    path('players/', views.jogadores_local),
]