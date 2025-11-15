from django.db import models

class Nota(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)

    class Meta:
        db_table = 'notas'

        verbose_name = 'apunte'
        verbose_name_plural = 'apuntes'

# Create your models here.
