from django.db import models
from indexapp.models import Cableoperadores
# Create your models here.
# Modelo de proyectos para ingresarlo a la base de datos

SI_NO_CHOICES = [
        ('si', 'Sí'),
        ('no', 'No'),
    ]
# Tipo de ingreso del proyecto
INGRESO = [
        ('Viabilidad', 'Viabilidad'),
        ('Desmonte', 'Desmonte'),
        ('Legalizacion', 'Legalizacion'),
    ]
ESTADO = [
        ('En_proceso', 'En proceso'),
        ('Cancelado', 'Cancelado'),
]
# Choices para departamentos
DEPARTAMENTOS = [
    ('atlantico', 'Atlantico'),
    ('magdalena', 'Magdalena'),
    ('la_guajira', 'La Guajira'),
]
class Proyectos(models.Model):
    cableoperador = models.ForeignKey(Cableoperadores, on_delete=models.CASCADE,verbose_name="Cableoperador")
    nombre = models.CharField(max_length=100, primary_key=True)
    responsable = models.CharField(
        max_length=100,
        verbose_name="Ejecutiva responsable",
    )
    TipoIngreso = models.CharField(max_length=100, choices=INGRESO, default='tipo1')
    Formato02 = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='no', verbose_name="¿Formato solicitud Uso de infraestructura?")
    Formato01 = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='no', verbose_name="¿Formato Caracterizacion de infraestructura?")
    plano = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='no', verbose_name="¿Tiene Plano de DWG?")
    Georreferencia = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='no', verbose_name="¿Tiene formato KMZ?")
    DocSolicitante = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='no', verbose_name="¿Tiene Documento del Solicitante?")
    MatriculaSolicitante = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='no', verbose_name="¿Tiene Matrícula del Solicitante?")
    FotoMarquilla = models.CharField(max_length=2, choices=SI_NO_CHOICES, default='no', verbose_name="¿Tiene Fotografía de la Marquilla a instalar?")
    tipo8 = models.PositiveIntegerField(verbose_name="Ingrese cantidad de Poste de Altura 8", default=0)
    tipo9 = models.PositiveIntegerField(verbose_name="Ingrese cantidad de Poste de Altura 9", default=0)
    tipo10 = models.PositiveIntegerField(verbose_name="Ingrese cantidad de Poste de Altura 10", default=0)
    tipo11 = models.PositiveIntegerField(verbose_name="Ingrese cantidad de Poste de Altura 11", default=0)
    tipo12 = models.PositiveIntegerField(verbose_name="Ingrese cantidad de Poste de Altura 12", default=0)
    tipo14 = models.PositiveIntegerField(verbose_name="Ingrese cantidad de Poste de Altura 14", default=0)
    tipo16 = models.PositiveIntegerField(verbose_name="Ingrese cantidad de Poste de Altura 16", default=0)
    departamento = models.CharField(max_length=20,choices=DEPARTAMENTOS)
    municipio = models.CharField(max_length=50,verbose_name="Municipio",)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    fecha_radicacion = models.DateField(null=True, blank=True)
    fecha_revision = models.DateField(null=True, blank=True)
    fecha_entrega = models.DateField(null=True, blank=True, auto_now_add=True)
    estado_ingreso = models.CharField(max_length=100, choices=ESTADO, default='En_proceso', verbose_name="Registro de estado del proyecto", null=True, blank=True)
    descripcion = models.TextField(max_length=1000, null=True, blank=True)
    class Meta:
        db_table = "proyectos"
    def __str__(self):
        return self.nombre