from django.db import models
from django.contrib.auth.models import User
from django.db import models
from sala.models import Sala

class Jogador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    sala_id = models.CharField(max_length=4, blank=True)
    name = models.CharField(max_length=30, blank=True)
    pista_banco = models.BooleanField(default=False)
    pista_bar = models.BooleanField(default=False)
    pista_penhores = models.BooleanField(default=False)
    pista_charutaria = models.BooleanField(default=False)
    pista_chaveiro = models.BooleanField(default=False)
    pista_docas = models.BooleanField(default=False)
    pista_carruagens = models.BooleanField(default=False)
    pista_farmacia = models.BooleanField(default=False)
    pista_hotel = models.BooleanField(default=False)
    pista_livraria = models.BooleanField(default=False)
    pista_museu = models.BooleanField(default=False)
    pista_parque = models.BooleanField(default=False)
    pista_syard = models.BooleanField(default=False)
    pista_teatro = models.BooleanField(default=False)
# Create your models here.
