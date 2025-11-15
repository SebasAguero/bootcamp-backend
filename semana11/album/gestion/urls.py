from django.urls import path
from .views import GestionAlbum

urlpatterns = [
    path('album', GestionAlbum.as_view()),
]