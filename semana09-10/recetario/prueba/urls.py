from django.urls import path
from .views import mostrarNotas

urlpatterns = [
  path('notas/', mostrarNotas),
]