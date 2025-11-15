from django.db import models
from uuid import uuid4

class Album(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    nombre = models.TextField()
    finalizado = models.BooleanField(default=False)

    class Meta:
        db_table = 'albums'

class Recuerdo(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    descripcion = models.TextField(null=True)
    albumId = models.ForeignKey(to=Album,
                                db_column='album_id',
                                on_delete=models.RESTRICT,
                                related_name='recuerdos')


    class Meta:
        db_table = 'recuerdos'

class Archivo(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    key = models.TextField(unique=True)
    path = models.TextField()
    extension = models.TextField()
    contentType = models.TextField(db_column='content_type')

    recuerdoId = models.ForeignKey(to=Recuerdo,
                                  db_column='recuerdo_id',
                                  on_delete=models.RESTRICT,
                                  related_name='archivos')
    
    class Meta:
        db_table = 'archivos'