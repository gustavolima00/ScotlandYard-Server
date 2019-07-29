from django.db import models

class Caso(models.Model):
    titulo = models.TextField()
    descricao = models.TextField()

    pista_banco = models.TextField()
    pista_bar = models.TextField()
    pista_penhores = models.TextField()
    pista_charutaria = models.TextField()
    pista_chaveiro = models.TextField()
    pista_docas = models.TextField()
    pista_carruagens = models.TextField()
    pista_farmacia = models.TextField()
    pista_hotel = models.TextField()
    pista_livraria = models.TextField()
    pista_museu = models.TextField()
    pista_parque = models.TextField()
    pista_syard = models.TextField()
    pista_teatro = models.TextField()

    solucao = models.TextField()


    # Create your models here.
