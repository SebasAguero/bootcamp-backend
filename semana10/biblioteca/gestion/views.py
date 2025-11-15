from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .permissions import EsAdmin, EsPersonal
from .models import Usuario, Categoria, Prestamo, Libro
from .serializers import UsuarioSerializer, CategoriaSerializer, PrestamoSerializer, LibroSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

@api_view(['POST'])
def registro(request):
    print(request.data)
    serializador = UsuarioSerializer(data=request.data)
    
    if serializador.is_valid():
      print(serializador.validated_data)

      nombre = serializador.validated_data.get('nombre')
      correo = serializador.validated_data.get('correo')
      apellido = serializador.validated_data.get('apellido')
      password = serializador.validated_data.get('password')

      nuevoUsuario = Usuario(nombre=nombre, correo=correo, apellido=apellido)
      nuevoUsuario.set_password(password)
      nuevoUsuario.save()

      return Response(data={
          'message': "Usuario registrado exitosamente."
      },status=status.HTTP_201_CREATED)
    
    else:
      return Response(data={
          'message': "Error al crear el usuario.",
          'content': serializador.errors
      },status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def usuario(request):
    print(request.auth)
    print(request.user)
    usuarioActual = request.user
    serializador = UsuarioSerializer(instance = usuarioActual)

    return Response(data={
        'content':'serializador.data'
    })

class GestionCategorias(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, EsAdmin]
    def get(self, request):
      categorias = Categoria.objects.all()
      resultado = CategoriaSerializer(instance=categorias, many=True)
      return Response(data={
        'message':'Las categorías son',
        'content': resultado.data
      })
    
    def post(self, request):
      serializador = CategoriaSerializer(data=request.data)
      if serializador.is_valid():
          nuevaCategoria = Categoria(**serializador.validated_data)
          nuevaCategoria.save()
          resultado = CategoriaSerializer(instance=nuevaCategoria)
          return Response(data={
          'message':'Categoría creada exitosamente',
          'content': resultado.data
        }, status=status.HTTP_201_CREATED)

      else:
          return Response(data={
          'message':'Error al crear la categoría',
          'content': serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)
      
class GestionCategoria(APIView):
    def get(self, request, id):
        categoriaEncontrada = Categoria.objects.filter(id=id).first()

        if not categoriaEncontrada:
            return Response(data={
                'message':'Categoría no encontrada'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategoriaSerializer(instance=categoriaEncontrada)

        return Response(data={
            'content': serializer.data
        })
    
    def put(self, request, id):
      categoriaEncontrada = Categoria.objects.filter(id=id).first()

      if not categoriaEncontrada:
            return Response(data={
                'message':'Categoría no encontrada'
            }, status=status.HTTP_404_NOT_FOUND)
      
      serializer = CategoriaSerializer(data=request.data)
      if serializer.is_valid():
        categoriaEncontrada.nombre = serializer.validated_data.get('nombre')
        categoriaEncontrada.save()

        resultado = CategoriaSerializer(instance=categoriaEncontrada)

        return Response(data={
            'message':'Categoría actualizada exitosamente',
            'content': resultado.data
        })
      
      else:
        return Response(data={
            'message':'Error al actualizar la categoría',
            'content': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
      
    def delete(self, request, id):
      categoriaEncontrada = Categoria.objects.filter(id=id).first()

      if not categoriaEncontrada:
            return Response(data={
                'message':'Categoría no encontrada'
            }, status=status.HTTP_404_NOT_FOUND)
      
      Categoria.objects.filter(id=id).delete()

      return Response(data={
          'message':'Categoría eliminada exitosamente'
      })
    
class GestionCategoriasGenerico(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, EsAdmin]

class GestionCategoriaGenerico(RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, EsAdmin]

    def destroy(self,request,pk):
        categoriaEncontrada = Categoria.objects.filter(id=pk).first()

        if not categoriaEncontrada:
              return Response(data={
                  'message':'Categoría no encontrada'
              }, status=status.HTTP_404_NOT_FOUND)
        
        Categoria.objects.filter(id=pk).delete()

        return Response(data={
            'message':'Categoría eliminada exitosamente'
        })
    
class GestionPrestamos(ListCreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    permission_classes = [IsAuthenticated, EsPersonal]

class GestionLibros(ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, EsAdmin]