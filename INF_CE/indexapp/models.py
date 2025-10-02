from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
# Cableoperadores - Aqui va la tabla de los cableoperadores
class Cableoperadores(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    nombre_largo = models.CharField(max_length=255, null=True, blank=True)
    NIT = models.CharField(max_length=100, null=True, blank=True)
    RegistroTic = models.BigIntegerField(null=True, blank=True)
    CodigoInterno = models.BigIntegerField(null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    Representante = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    correo = models.EmailField(max_length=100, null=True, blank=True)
    ejecutiva = models.ForeignKey(
        User,
        # Filtra a los usuarios cuya ID de grupo esté en el conjunto de IDs del grupo 'Ejecutivas'
        limit_choices_to={'groups__name': 'Ejecutivas'},
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Ejecutiva Asignada"
    )
    
    class Meta:
        db_table = "cableoperadores"
    def __str__(self):
        return self.nombre