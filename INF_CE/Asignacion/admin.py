# admin.py

from django.contrib import admin
from django_select2.forms import Select2Widget
from .models import Asignacion_proyectos
from django import forms # Importa el módulo forms

class AsignacionProyectosAdminForm(forms.ModelForm):
    class Meta:
        model = Asignacion_proyectos
        fields = '__all__'
        widgets = {
            'persona_asignada': Select2Widget,
        }

class AsignacionProyectosAdmin(admin.ModelAdmin):
    form = AsignacionProyectosAdminForm
    list_display = ('nombre_proyecto', 'estado', 'persona_asignada', 'fecha_asignacion')
    list_filter = ('estado', 'persona_asignada')

admin.site.register(Asignacion_proyectos, AsignacionProyectosAdmin)