from rest_framework import serializers
from .models import Album, Archivo, Recuerdo

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class RecuerdoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recuerdo
        fields = '__all__'

class RutaFirmadaSerializer(serializers.Serializer):
    key = serializers.CharField(required=True)
    contentType = serializers.CharField(required=True)

class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        fields = '__all__'