from django.contrib import admin
from django_select2.forms import Select2Widget
from django import forms # Importa el módulo forms
from .models import Proyectos
# Register your models here.
class ProyectosAdminForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = '__all__'
        widgets = {
            'cableoperador': Select2Widget(attrs={
            'data-placeholder': 'Seleccione un cableoperador',
            'data-allow-clear': 'true',
            })
        }

class ProyectosAdmin(admin.ModelAdmin):
    form = ProyectosAdminForm
    list_display = ('nombre', 'responsable', 'departamento', 'municipio', 'fecha_inicio', 'fecha_fin', 'cableoperador')
    list_filter = ('departamento', 'municipio', 'cableoperador')

admin.site.register(Proyectos, ProyectosAdmin)