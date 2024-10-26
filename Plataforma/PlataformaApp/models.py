from django.db import models
from django.core import validators

# Create your models here.

class Plataforma(models.Model):
    TIPOS = [
        ('Consola', 'Consola'),
        ('PC', 'PC'),
        ('Movil', 'Movil')
    ]

    tipo = models.CharField(max_length=20, choices=TIPOS)
    generacion = models.CharField(max_length=20)
    almacenamiento = models.IntegerField()
    fabricante = models.CharField(max_length=20)
    precio = models.FloatField(max_length=5)
    
def __str__(self):
   return Plataforma