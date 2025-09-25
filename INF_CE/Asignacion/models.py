from django.db import models
from indexapp.models import Proyectos
from django.contrib.auth.models import User, Group # Importa los modelos de usuario y grupo

# Create your models here

class Asignacion_proyectos(models.Model):
    nombre_proyecto = models.OneToOneField(Proyectos, on_delete=models.CASCADE, primary_key=True)
    nombre_ingeniero = models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        # First, save the current Asignacion_proyectos instance
        super().save(*args, **kwargs)

        # Get the related Proyectos instance
        proyecto = self.nombre_proyecto

        # Check if the estado is different from estado_ingreso
        if proyecto.estado_ingreso != self.estado:
            # Update the estado_ingreso of the linked Proyectos object
            proyecto.estado_ingreso = self.estado
            proyecto.save(update_fields=['estado_ingreso'])
    # Cambiamos persona_asignada a un ForeignKey que apunta al modelo User
    persona_asignada = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.CharField(max_length=100, verbose_name="Estado del Proyecto", default='En_progreso')
    fecha_asignacion = models.DateField(null=True, blank=True)
    observaciones = models.TextField(max_length=1000, null=True, blank=True)
    class Meta:
        db_table = "asignacion_proyectos"
    def __str__(self):
        return self.nombre_proyecto.nombre
        
