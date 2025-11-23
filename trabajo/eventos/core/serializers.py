from rest_framework import serializers
from .models import Evento, Participante

class ParticipanteSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='name')
    email = serializers.EmailField()
    createdAt = serializers.DateTimeField(source='created_at', read_only=True)
    updatedAt = serializers.DateTimeField(source='updated_at', read_only=True)

    class Meta:
        model = Participante
        fields = ['id', 'nombre', 'email', 'createdAt', 'updatedAt']


class EventoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='name')
    fecha = serializers.DateTimeField(source='date')
    lugar = serializers.CharField(source='location')
    descripcion = serializers.CharField(source='description')
    participantes = ParticipanteSerializer(source='participants', many=True, read_only=True)
    createdAt = serializers.DateTimeField(source='created_at', read_only=True)
    updatedAt = serializers.DateTimeField(source='updated_at', read_only=True)

    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fecha', 'lugar', 'descripcion', 'createdAt', 'updatedAt', 'participantes']