from django.db import models
from django.contrib.postgres.fields import ArrayField
from caso.models import Caso
import uuid

def generate_key():
    uid = uuid.uuid4()
    return uid.int%100000

class Sala(models.Model):
    id = models.IntegerField(primary_key=True, default=generate_key, editable=False)
    caso_id = models.CharField(max_length=10 ,blank=True)
    jogadores = models.IntegerField(default=0)
# Create your models here.

