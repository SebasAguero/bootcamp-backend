from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .models import Album,Archivo,Recuerdo
from .serializers import AlbumSerializer

class GestionAlbum(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer