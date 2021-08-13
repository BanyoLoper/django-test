from django.db import models
from django.db.models.base import Model

# Create your models here.
class Usuario(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


