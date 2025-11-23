from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Evento, Participante
from .serializers import EventoSerializer, ParticipanteSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['date']
    search_fields = ['name', 'location', 'description']

    @action(detail=True, methods=['post'])
    def agregar_participante(self, request, pk=None):
        evento = self.get_object()
        participante_id = request.data.get('participante_id')

        try:
            participante = Participante.objects.get(id=participante_id)
        except Participante.DoesNotExist:
            return Response({'error': 'El participante no existe'}, status=status.HTTP_404_NOT_FOUND)

        if participante in evento.participants.all():
            return Response({'error': 'El participante ya está registrado en el evento'}, status=status.HTTP_400_BAD_REQUEST)

        evento.participants.add(participante)
        return Response({'success': 'Participante agregado'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def quitar_participante(self, request, pk=None):
        evento = self.get_object()
        participante_id = request.data.get('participante_id')

        try:
            participante = Participante.objects.get(id=participante_id)
        except Participante.DoesNotExist:
            return Response({'error': 'El participante no existe'}, status=status.HTTP_404_NOT_FOUND)

        evento.participants.remove(participante)
        return Response({'success': 'Participante quitado'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def participantes(self, request, pk=None):
        evento = self.get_object()
        participantes = evento.participants.all()
        serializer = ParticipanteSerializer(participantes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer