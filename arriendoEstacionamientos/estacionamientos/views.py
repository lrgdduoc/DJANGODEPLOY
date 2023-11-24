from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .estacionamientoSerializer import estacionamientoSerializer
from .models import estacionamiento

class estacionamientoViewSet(viewsets.ModelViewSet):
    queryset = estacionamiento.objects.all()

    def get_serializer_class(self):
        return estacionamientoSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
