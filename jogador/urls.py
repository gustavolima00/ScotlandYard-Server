from django.urls import include, path
from . import views

urlpatterns = [
    path('all/', views.todos_jogadores),
    path('update/', views.update_jogador),
    path('update_hints/', views.update_hints),
    path('get/', views.get_jogador),
    path('reset/', views.reset_jogador),
]