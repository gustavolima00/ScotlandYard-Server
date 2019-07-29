from django.db import models
from django.contrib.auth.models import User

class Jogador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    
    pista_banco = models.BooleanField()
    pista_bar = models.BooleanField()
    pista_penhores = models.BooleanField()
    pista_charutaria = models.BooleanField()
    pista_chaveiro = models.BooleanField()
    pista_docas = models.BooleanField()
    pista_carruagens = models.BooleanField()
    pista_farmacia = models.BooleanField()
    pista_hotel = models.BooleanField()
    pista_livraria = models.BooleanField()
    pista_museu = models.BooleanField()
    pista_parque = models.BooleanField()
    pista_syard = models.BooleanField()
    pista_teatro = models.BooleanField()
# Create your models here.
