from django.urls import path
from .views import GestionAlbum, alternarAlbumEstado, GestionRecuerdo, crearRutaFirmadaArchivo, GestionArchivos, GestionArchivo

urlpatterns = [
    path('album', GestionAlbum.as_view()),
    path('alternar-album-estado/<id>', alternarAlbumEstado),
    path('recuerdo', GestionRecuerdo.as_view()),
    path('crear-url-firmada', crearRutaFirmadaArchivo),
    path('archivos', GestionArchivos.as_view()),
    path('archivo/<id>', GestionArchivo.as_view())
]