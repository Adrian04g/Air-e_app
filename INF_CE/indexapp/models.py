from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
# Cableoperadores - Aqui va la tabla de los cableoperadores
Rliquidacion = [
    ('Calendarios', 'Calendarios'),
    ('Habiles', 'Habiles'),
]
ESTADOS_CONTRATO = [
    ('Contratado' , 'Contratado'),
    ('Finalizado' , 'Finalizado'),
    ('En_Renovacion' , 'En Renovacion'),
    ('Renovacion_firma_prst' , 'En Renovacion - Firma PRST'),
    ('Renovacion_firma_air_e' , 'En Renovacion - Firma AIR-E'),
    ('nuevo_firma_prst' , 'Nuevo - Firma PRST'),
    ('nuevo_firma_air_e' , 'Nuevo - Firma AIR-E'),
    ('En_Gestion' , 'En Gestion'),
    ('Sin_usos' , 'Sin Usos'),
]
class Cableoperadores(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    nombre_largo = models.CharField(max_length=255, null=True, blank=True, unique=True)
    NIT = models.IntegerField(null=True, blank=True, unique=True)
    Digito_verificacion = models.IntegerField(null=True, blank=True)
    RegistroTic = models.BigIntegerField(null=True, blank=True)
    CodigoInterno = models.BigIntegerField(null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    Representante = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.BigIntegerField()
    correo = models.EmailField(max_length=100)
    ejecutiva = models.CharField(max_length=100)
    observaciones = models.TextField(max_length=1000)
    estado = models.CharField(max_length=100, choices=ESTADOS_CONTRATO)
    vencimiento_factura = models.IntegerField(null=True, blank=True)
    preliquidacion_num = models.IntegerField(null=True, blank=True)
    preliquidacion_letra = models.CharField(max_length=100,null=True, blank=True)
    respuesta_preliquidacion = models.CharField(choices=Rliquidacion, max_length=100,null=True, blank=True)
    
    class Meta:
        db_table = "cableoperadores"
    def __str__(self):
        return self.nombre