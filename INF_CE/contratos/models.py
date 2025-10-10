from django.db import models
from indexapp.models import Cableoperadores
from django.db.models import Q, UniqueConstraint
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
VIGENCIA_AMPARO_CHOICES = [
    ('Igual_a_Duracion_de_Contrato_mas_12_Meses' , 'Igual a Duración de Contrato + 12 Meses'),
    ('Igual_a_Duracion_de_Contrato_mas_6_Meses' , 'Igual a Duración de Contrato + 6 Meses'),
    ('Igual_a_Duracion_de_Contrato_mas_4_Meses' , 'Igual a Duración de Contrato + 4 Meses'),
    ('Igual_a_Duracion_de_Contrato_mas_2_Meses' , 'Igual a Duración de Contrato + 2 Meses'),
]
MONTO_ASEGURADO_POLIZA_CUMPLIMIENTO_CHOICES = [
    ('15%_valor_contrato', '15% Valor del Contrato'),
    ('20%_valor_contrato', '20% Valor del Contrato'),
    ('30%_valor_contrato', '30% Valor del Contrato'),
    ('20%_valor_base_constitucion_poliza', '20% Valor base de Constitución de Póliza'),
    ('30%_valor_base_constitucion_poliza', '30% Valor base de Constitución de Póliza'),
]
MONTO_ASEGURADO_POLIZA_RCE_CHOICES = [
    ('no_inferior_100_SMLMV', 'No inferior a 100 SMLMV'),
    ('no_inferior_200_SMLMV', 'No inferior a 200 SMLMV'),
    ('no_inferior_300_SMLMV', 'No inferior a 300 SMLMV'),
]
class Contratos(models.Model):
    cableoperador = models.ForeignKey(Cableoperadores, on_delete=models.PROTECT)
    tipo_contrato = models.CharField(max_length=100, choices=CLASIFICACION)
    estado_contrato = models.CharField(max_length=100, choices=ESTADOS_CONTRATO)
    duracion_anos = models.IntegerField(verbose_name="Duración en años")
    inicio_vigencia = models.DateField()
    fin_vigencia = models.DateField()
    valor_contrato = models.DecimalField(max_digits=20, decimal_places=2)
    # Campos para la Póliza de Cumplimiento
    numero_poliza_cumplimiento = models.CharField(max_length=100, blank=True, null=True)
    vigencia_amparo_poliza_cumplimiento = models.CharField(max_length=100, blank=True, null=True, choices=VIGENCIA_AMPARO_CHOICES)
    inicio_vigencia_poliza_cumplimiento = models.DateField(blank=True, null=True)
    fin_vigencia_poliza_cumplimiento = models.DateField(blank=True, null=True)
    monto_asegurado_poliza_cumplimiento = models.CharField(max_length=100, blank=True, null=True, choices=MONTO_ASEGURADO_POLIZA_CUMPLIMIENTO_CHOICES)
    valor_monto_asegurado_poliza_cumplimiento = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    valor_asegurado_poliza_cumplimiento = models.CharField(max_length=100, blank=True, null=True)
    inicio_amparo_poliza_cumplimiento = models.DateField(blank=True, null=True)
    fin_amparo_poliza_cumplimiento = models.DateField(blank=True, null=True)
    expedicion_poliza_cumplimiento = models.DateField(blank=True, null=True)
    # Campos para la Póliza de RCE
    numero_poliza_rce = models.CharField(max_length=100, blank=True, null=True)
    vigencia_amparo_poliza_rce = models.CharField(max_length=100, blank=True, null=True, choices=VIGENCIA_AMPARO_CHOICES)
    inicio_vigencia_poliza_rce = models.DateField(blank=True, null=True)
    fin_vigencia_poliza_rce = models.DateField(blank=True, null=True)
    monto_asegurado_poliza_rce = models.CharField(max_length=100, blank=True, null=True, choices=MONTO_ASEGURADO_POLIZA_RCE_CHOICES)
    valor_monto_asegurado_poliza_rce = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    valor_asegurado_poliza_rce = models.CharField(max_length=100, blank=True, null=True)
    inicio_amparo_poliza_rce = models.DateField(blank=True, null=True)
    fin_amparo_poliza_rce = models.DateField(blank=True, null=True)
    expedicion_poliza_rce = models.DateField(blank=True, null=True)
    tomador = models.CharField(max_length=100, blank=True, null=True)
    aseguradora = models.CharField(max_length=100, blank=True, null=True)
    fecha_radicacion = models.IntegerField()
    tipo_fecha_radicacion = models.CharField(max_length=100, choices=TIPO_FECHA_RADICACION_CONTRATO)
    fecha_preliquidacion = models.DateField(blank=True, null=True)
    
    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['estado_contrato'],
                # Aplica la restricción SOLAMENTE cuando estado_contrato es 'Vigente'
                condition=Q(estado_contrato='Vencido'), 
                name='unique_Vencido_contrato'
            )
        ]
        db_table = "Contratos"
    
    def __str__(self):
        return f"Contrato de {self.cableoperador.nombre}"