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
            'Digito_verificacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digito de verificación del cableoperador'
            }),
            'RegistroTic': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Registro TIC del cableoperador'
            }),
            'CodigoInterno': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Código interno del cableoperador'
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
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Observaciones',
                'rows': 4,
            }),
            'estado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Estado del cableoperador',
                'max_length': 100
            }),
            'vencimiento_factura': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Vencimiento de la factura'
            }),
            'preliquidacion_num': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de preliquidación'
            }),
            'preliquidacion_letra': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Letra de preliquidación',
                'max_length': 100
            }),
            'respuesta_preliquidacion': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Letra de preliquidación',
                'max_length': 100
            }),
            'ejecutiva': Select2Widget(attrs={
                'class': 'form-control'
            }),
        }

        
        
