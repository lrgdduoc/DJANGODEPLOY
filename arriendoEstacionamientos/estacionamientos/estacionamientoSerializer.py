from rest_framework import serializers

from .models import estacionamiento

class estacionamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = estacionamiento
        fields = ('id', 'nombre_estacionamieto', 'direccion', 'capacidad', 'fecha_publicacion', 'precio')