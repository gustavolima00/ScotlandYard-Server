from django.db import models
from sala.models import Sala

class Action(models.Model):
    time = models.DateTimeField(auto_now_add= True)
    room = models.ForeignKey(Sala, on_delete=models.CASCADE)
    text = models.TextField()

