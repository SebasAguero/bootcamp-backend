from rest_framework import serializers
from .models import Album, Archivo, Recuerdo

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'