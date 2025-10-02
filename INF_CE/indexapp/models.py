from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
# Cableoperadores - Aqui va la tabla de los cableoperadores
Rliquidacion = [
    ('Calendarios', 'Calendarios'),
    ('Habiles', 'Habiles'),
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
    estado = models.CharField(max_length=100)
    vencimiento_factura = models.IntegerField()
    preliquidacion_num = models.IntegerField()
    preliquidacion_letra = models.CharField(max_length=100)
    respuesta_preliquidacion = models.CharField(choices=Rliquidacion, max_length=100)
    
    class Meta:
        db_table = "cableoperadores"
    def __str__(self):
        return self.nombre
    
    
class Cable(models.Model):
    tipo8 = models.PositiveIntegerField(verbose_name="Cantidad de uso de cables en postes de 8 metros", default=0)
    tipo10 = models.PositiveIntegerField(verbose_name="Cantidad de uso de cables en postes de 10 metros", default=0)
    tipo12 = models.PositiveIntegerField(verbose_name="Cantidad de uso de cables en postes de 12 metros", default=0)
    tipo14 = models.PositiveIntegerField(verbose_name="Cantidad de uso de cables en postes de 14 metros", default=0)
    tipo15 = models.PositiveIntegerField(verbose_name="Cantidad de uso de cables en postes de 15 metros", default=0)
    tipo16 = models.PositiveIntegerField(verbose_name="Cantidad de uso de cables en postes de 16 metros", default=0)
    tipo20 = models.PositiveIntegerField(verbose_name="Cantidad de uso de cables en postes de 20 metros", default=0)
    def __str__(self):
        return str(self.pk)
class Caja_empalme(models.Model):
    tipo8 = models.PositiveIntegerField(verbose_name="Cantidad de uso de caja de empalme en postes de 8 metros", default=0)
    tipo10 = models.PositiveIntegerField(verbose_name="Cantidad de uso de caja de empalme en postes de 10 metros", default=0)
    tipo12 = models.PositiveIntegerField(verbose_name="Cantidad de uso de caja de empalme en postes de 12 metros", default=0)
    tipo14 = models.PositiveIntegerField(verbose_name="Cantidad de uso de caja de empalme en postes de 14 metros", default=0)
    tipo15 = models.PositiveIntegerField(verbose_name="Cantidad de uso de caja de empalme en postes de 15 metros", default=0)
    tipo16 = models.PositiveIntegerField(verbose_name="Cantidad de uso de caja de empalme en postes de 16 metros", default=0)
    tipo20 = models.PositiveIntegerField(verbose_name="Cantidad de uso de caja de empalme en postes de 20 metros", default=0)
    def __str__(self):
        return str(self.pk)
class Reserva(models.Model):
    tipo8 = models.PositiveIntegerField(verbose_name="Cantidad de uso de reserva en postes de 8 metros", default=0)
    tipo10 = models.PositiveIntegerField(verbose_name="Cantidad de uso de reserva en postes de 10 metros", default=0)
    tipo12 = models.PositiveIntegerField(verbose_name="Cantidad de uso de reserva en postes de 12 metros", default=0)
    tipo14 = models.PositiveIntegerField(verbose_name="Cantidad de uso de reserva en postes de 14 metros", default=0)
    tipo15 = models.PositiveIntegerField(verbose_name="Cantidad de uso de reserva en postes de 15 metros", default=0)
    tipo16 = models.PositiveIntegerField(verbose_name="Cantidad de uso de reserva en postes de 16 metros", default=0)
    tipo20 = models.PositiveIntegerField(verbose_name="Cantidad de uso de reserva en postes de 20 metros", default=0)
    def __str__(self):
        return str(self.pk)
class Nap(models.Model):
    tip8 = models.PositiveIntegerField(verbose_name="Cantidad de uso nap en postes de 8 metros", default=0)
    tip10 = models.PositiveIntegerField(verbose_name="Cantidad de uso nap en postes de 10 metros", default=0)
    tip12 = models.PositiveIntegerField(verbose_name="Cantidad de uso nap en postes de 12 metros", default=0)
    tip14 = models.PositiveIntegerField(verbose_name="Cantidad de uso nap en postes de 14 metros", default=0)
    tip15 = models.PositiveIntegerField(verbose_name="Cantidad de uso nap en postes de 15 metros", default=0)
    tip16 = models.PositiveIntegerField(verbose_name="Cantidad de uso nap en postes de 16 metros", default=0)
    tip20 = models.PositiveIntegerField(verbose_name="Cantidad de uso nap en postes de 20 metros", default=0)
    def __str__(self):
        return str(self.pk)
class Usos(models.Model):
    cables = models.ForeignKey(Cable, on_delete=models.CASCADE)
    cajas_empalme = models.ForeignKey(Caja_empalme, on_delete=models.CASCADE)
    reservas = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    naps = models.ForeignKey(Nap, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.pk)
CLASIFICACION = [
    ('tipo1' , 'tipo1'),
    ('tipo2' , 'tipo2'),
    ('tipo3' , 'tipo3'),
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
class Contratos(models.Model):
    cableoperador = models.ForeignKey(Cableoperadores, on_delete=models.PROTECT)
    usos = models.ForeignKey(Usos, on_delete=models.PROTECT)
    numero_contrato = models.CharField(max_length=100, unique=True)
    tipo_contrato = models.CharField(max_length=100, choices=CLASIFICACION)
    estado_contrato = models.CharField(max_length=100, choices=CLASIFICACION)
    duracion_anos = models.IntegerField()
    inicio_vigencia = models.DateField()
    fin_vigencia = models.DateField()
    valor_contrato = models.DecimalField(max_digits=20, decimal_places=2)
    Garantia = models.CharField(max_length=100)
    fecha_radicacion = models.DateField()
    tipo_fecha_radicacion = models.CharField(max_length=100)
    class Meta:
        db_table = "contratos"
    def __str__(self):
        return f"Contrato {self.numero_contrato} de {self.cableoperador.nombre}"