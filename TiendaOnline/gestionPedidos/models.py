#Gestiona los modelos

from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    tfno = models.CharField(max_length=7)

class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    #Se me parece a un toString de java
    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)

class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()