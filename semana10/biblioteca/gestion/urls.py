from django.urls import path
from .views import (registro,
                    usuario,
                    GestionCategorias,
                    GestionCategoria,
                    GestionCategoriasGenerico,
                    GestionCategoriaGenerico,
                    GestionPrestamos,
                    GestionLibros)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('registro/',registro),
    path('login/',TokenObtainPairView.as_view()),
    path('perfil', usuario),
    path('categorias', GestionCategorias.as_view()),
    path('categoria/<id>', GestionCategoria.as_view()),
    path('categorias-generic', GestionCategoriasGenerico.as_view()),
    path('categoria-generic/<pk>', GestionCategoriaGenerico.as_view()),
    path('prestamos', GestionPrestamos.as_view()),
    path('libros', GestionLibros.as_view()),
]