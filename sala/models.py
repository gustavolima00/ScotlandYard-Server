from django.db import models
from django.contrib.postgres.fields import ArrayField
from caso.models import Caso
import uuid

def generate_key():
    uid = uuid.uuid4()
    return str(uid.int%100000)

class Sala(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=generate_key, editable=False)
    caso_id = models.CharField(max_length=10)
    jogadores = models.IntegerField(default=0)
    log_actions = []
# Create your models here.

