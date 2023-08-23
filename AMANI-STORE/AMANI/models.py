from django.db import models
from datetime import datetime

# Create your models here.
class Amani(models.Model):
    nome_card = models.CharField(max_length=200)
    description = models.TextField()
    path = models.ImageField()
    date_create = models.DateTimeField(default=datetime.now, blank =True)