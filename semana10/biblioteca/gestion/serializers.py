from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Usuario, Categoria, Prestamo, Libro
from django_ulid.serializers import ULIDField

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['groups', 'user_permissions', 'is_superuser', 'is_staff', 'is_active', 'last_login']

        extra_kwargs = {
            'password': {'write_only': True}
        }
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class PrestamoSerializer(ModelSerializer):
    def to_representation(self, instance):
      return{
          'id': str(instance.id),
          'libroId': str(instance.libroId),
          'usuarioId': str(instance.usuarioId),
          'fecha': instance.fecha,
          'estado': instance.estado
      }
    class Meta:
        model = Prestamo
        fields = '__all__'

class LibroSerializer(ModelSerializer):
  def to_representation(self, instance):
      return{
          'id': str(instance.id),
          'nombre': instance.nombre,
          'autor': instance.autor,
          'edicion': instance.edicion,
          'descripcion': instance.descripcion,
          'categoriaId': str(instance.categoriaId.id)
      }
  
  class Meta:
      model = Libro
      fields = '__all__'