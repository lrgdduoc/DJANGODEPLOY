from django.contrib import admin
from django.urls import path

from estacionamientos.views import estacionamientoViewSet

urlpatterns = [
    path('estacionamientos/', estacionamientoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('estacionamientos/<int:pk>', estacionamientoViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}))
]
