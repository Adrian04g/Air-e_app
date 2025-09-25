from django.contrib import admin
from django_select2.forms import Select2Widget
from django import forms # Importa el módulo forms
from django.contrib.auth.models import User
from .models import Cableoperadores, Proyectos
# Register your models here.
admin.site.register(Cableoperadores)

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

# Unregister the User model from the admin site
admin.site.unregister(User)
# Admin 
from django.contrib.auth.admin import UserAdmin
@admin.register(User)
class NewAdmin(UserAdmin):
    pass