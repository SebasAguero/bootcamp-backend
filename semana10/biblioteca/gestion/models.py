from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django_ulid.models import default, ULIDField

class ManejadorUsuario(BaseUserManager):
  def create_superuser(self, nombre, correo, password):
    if not correo:
      raise ValueError('El correo es obligatorio')
    
    correoNormalizado = self.normalize_email(correo)

    nuevoUsuario = self.model(correo=correoNormalizado, nombre=nombre)
    nuevoUsuario.set_password(password)
    nuevoUsuario.is_superuser = True
    nuevoUsuario.is_staff = True
    nuevoUsuario.save()

TIPO_USUARIO = [
  ('1', 'ADMIN'),
  ('2', 'USUARIO'),
  ('3', 'PERSONAL')
]

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = ULIDField(primary_key=True, default=default)
    nombre = models.TextField(null=False)
    apellido = models.TextField()
    correo = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    tipoUsuario = models.TextField(db_column='tipo_usuario', choices=TIPO_USUARIO)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']
    objects = ManejadorUsuario()

    class Meta:
        db_table = 'usuarios'

class Categoria(models.Model):
    id = ULIDField(primary_key=True, default=default)
    nombre = models.TextField(unique=True)

    class Meta:
        db_table = 'categorias'
    
class Libro(models.Model):
    id = ULIDField(primary_key=True, default=default)
    nombre = models.TextField(null=False)
    autor = models.TextField(null=False)
    edicion = models.TextField(null=False)
    descripcion = models.TextField()
    categoriaId = models.ForeignKey(to=Categoria, on_delete=models.PROTECT, db_column='categoria_id')
    class Meta:
        db_table = 'libros'

class Prestamo(models.Model):
  id = ULIDField(primary_key=True, null=False, default=default)
  libroId = models.ForeignKey(to=Libro, on_delete=models.PROTECT, db_column='libro_id', related_name='prestamos')
  usuarioId = models.ForeignKey(to=Usuario, on_delete=models.PROTECT, db_column='usuario_id', related_name='librosPrestadosUsuarios')
  fecha = models.DateField(null=False)
  estado = models.TextField()

  class Meta:
    db_table = 'prestamos'