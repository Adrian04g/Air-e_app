from django.db import models
from indexapp.models import Cableoperadores
# Create your models here.
class Cable(models.Model):
    # La clave OneToOneField asegura que solo haya un registro de Cable por Contrato
    contrato = models.OneToOneField(
        'Contratos', # Apunta al modelo Contratos
        on_delete=models.CASCADE, 
        primary_key=True, # Hace que este campo sea la PK, forzando la unicidad
        verbose_name="Contrato Asociado"
    )
    tipo8 = models.PositiveIntegerField(verbose_name="8 metros", default=0)
    tipo10 = models.PositiveIntegerField(verbose_name="10 metros", default=0)
    tipo12 = models.PositiveIntegerField(verbose_name="12 metros", default=0)
    tipo14 = models.PositiveIntegerField(verbose_name="14 metros", default=0)
    tipo15 = models.PositiveIntegerField(verbose_name="15 metros", default=0)
    tipo16 = models.PositiveIntegerField(verbose_name="16 metros", default=0)
    tipo20 = models.PositiveIntegerField(verbose_name="20 metros", default=0)
    class Meta:
        db_table = "Cables"
    def __str__(self):
        return f"Cables de Contrato {self.contrato.numero_contrato}"

class Caja_empalme(models.Model):
    contrato = models.OneToOneField(
        'Contratos', 
        on_delete=models.CASCADE, 
        primary_key=True,
        verbose_name="Contrato Asociado"
    )
    tipo8 = models.PositiveIntegerField(verbose_name="8 metros", default=0)
    tipo10 = models.PositiveIntegerField(verbose_name="10 metros", default=0)
    tipo12 = models.PositiveIntegerField(verbose_name="12 metros", default=0)
    tipo14 = models.PositiveIntegerField(verbose_name="14 metros", default=0)
    tipo15 = models.PositiveIntegerField(verbose_name="15 metros", default=0)
    tipo16 = models.PositiveIntegerField(verbose_name="16 metros", default=0)
    tipo20 = models.PositiveIntegerField(verbose_name="20 metros", default=0)
    class Meta:
        db_table = "Cajas_empalme"
    def __str__(self):
        return f"Cajas de Contrato {self.contrato.numero_contrato}"

class Reserva(models.Model):
    contrato = models.OneToOneField(
        'Contratos', 
        on_delete=models.CASCADE, 
        primary_key=True,
        verbose_name="Contrato Asociado"
    )
    tipo8 = models.PositiveIntegerField(verbose_name="8 metros", default=0)
    tipo10 = models.PositiveIntegerField(verbose_name="10 metros", default=0)
    tipo12 = models.PositiveIntegerField(verbose_name="12 metros", default=0)
    tipo14 = models.PositiveIntegerField(verbose_name="14 metros", default=0)
    tipo15 = models.PositiveIntegerField(verbose_name="15 metros", default=0)
    tipo16 = models.PositiveIntegerField(verbose_name="16 metros", default=0)
    tipo20 = models.PositiveIntegerField(verbose_name="20 metros", default=0)
    class Meta:
        db_table = "Reservas"

    def __str__(self):
        return f"Reservas de Contrato {self.contrato.numero_contrato}"

class Nap(models.Model):
    contrato = models.OneToOneField(
        'Contratos', 
        on_delete=models.CASCADE, 
        primary_key=True,
        verbose_name="Contrato Asociado"
    )
    tip8 = models.PositiveIntegerField(verbose_name="8 metros", default=0)
    tip10 = models.PositiveIntegerField(verbose_name="10 metros", default=0)
    tip12 = models.PositiveIntegerField(verbose_name="12 metros", default=0)
    tip14 = models.PositiveIntegerField(verbose_name="14 metros", default=0)
    tip15 = models.PositiveIntegerField(verbose_name="15 metros", default=0)
    tip16 = models.PositiveIntegerField(verbose_name="16 metros", default=0)
    tip20 = models.PositiveIntegerField(verbose_name="20 metros", default=0)
    class Meta:
        db_table = "Naps"

# Definiciones de Choices
CLASIFICACION = [
    ('tipo1' , 'tipo1'),
    ('tipo2' , 'tipo2'),
    ('tipo3' , 'tipo3'),
]
ESTADOS_CONTRATO = [
    ('Vigente' , 'Vigente'),
    ('Vencido' , 'Vencido'),
]
TIPO_FECHA_RADICACION_CONTRATO = [
    ('fija' , 'Fija'),
    ('dinamica' , 'Dinámica'),
]
GARANTIA_CHOICES = [
    ('poliza_rce', 'Póliza de RCE'),
    ('poliza_cumplimiento', 'Póliza de Cumplimiento'),
]
class Contratos(models.Model):
    cableoperador = models.ForeignKey(Cableoperadores, on_delete=models.PROTECT)
    tipo_contrato = models.CharField(max_length=100, choices=CLASIFICACION)
    estado_contrato = models.CharField(max_length=100, choices=ESTADOS_CONTRATO)
    duracion_anos = models.IntegerField()
    inicio_vigencia = models.DateField()
    fin_vigencia = models.DateField()
    valor_contrato = models.DecimalField(max_digits=20, decimal_places=2)
    Garantia = models.CharField(max_length=100, choices=GARANTIA_CHOICES)
    fecha_radicacion = models.IntegerField()
    tipo_fecha_radicacion = models.CharField(max_length=100, choices=TIPO_FECHA_RADICACION_CONTRATO)
    
    class Meta:
        db_table = "Contratos"
    
    def __str__(self):
        return f"Contrato de {self.cableoperador.nombre}"