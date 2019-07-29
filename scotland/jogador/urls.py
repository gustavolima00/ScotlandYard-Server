from django.urls import include, path
from . import views

urlpatterns = [
    path('all/', views.todos_jogadores),
    path('update/', views.update_jogador),
    path('get/', views.get_jogador),
]