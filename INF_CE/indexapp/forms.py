from django import forms
from .models import Cableoperadores
from django.contrib.auth.models import User, Group
from django_select2.forms import Select2Widget
# Opciones para el campo de estado del proyecto
SHIFT_CHOICES = [
    ('1', 'En Progreso'),
    ('2', 'Completado'),
    ('3', 'Pendiente'),
]

    

class CableoperadoresModelForm(forms.ModelForm):
    class Meta:
        model = Cableoperadores
        fields = '__all__'
        exclude = ['ejecutiva']