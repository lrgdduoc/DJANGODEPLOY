from django.db import models

# Create your models here.
class estacionamiento(models.Model):
    nombre_estacionamieto = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    capacidad = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre_estacionamieto
