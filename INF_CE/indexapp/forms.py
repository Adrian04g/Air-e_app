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
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del cableoperador'
            }),
            'nombre_largo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre largo del cableoperador'
            }),
            'NIT': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'NIT del cableoperador'
            }),
            'RegistroTic': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Registro TIC del cableoperador'
            }),
            'CodigoInterno': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Codigo Interno del cableoperador'
            }), 
            
            'pais': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Pais del cableoperador'
            }),
            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ciudad del cableoperador'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección del cableoperador'
            }),
            'Representante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Representante del cableoperador'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefono del cableoperador'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo del cableoperador'
            }),
            'ejecutiva': forms.Select(attrs={
                'class': 'form-DateInput',
                'widget': Select2Widget
                
            }),
        }
        
        