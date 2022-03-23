from django.db import models
from django.db import models

from dispositivo.models import Dispositivo


class Bitacora(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, related_name="bitacora", on_delete=models.CASCADE)
    potencia = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)