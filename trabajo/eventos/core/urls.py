from rest_framework import routers
from django.urls import path, include
from .views import EventoViewSet, ParticipanteViewSet

router = routers.DefaultRouter()
router.register(r'eventos', EventoViewSet, basename='evento')
router.register(r'participantes', ParticipanteViewSet, basename='participante')

urlpatterns = [
    path('', include(router.urls)),
]