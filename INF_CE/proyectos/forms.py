from django import forms
from .models import Proyectos
from django_select2.forms import Select2Widget
# Formulario con ModelForms
class ProyectosModelForm(forms.ModelForm):

    class Meta:
        model = Proyectos
        fields = '__all__'
        exclude = ['responsable']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del proyecto'
            }),
            'TipoIngreso': forms.Select(attrs={
                'class': 'form-control'
            }),
            'departamento': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Seleccione un departamento',
            }),
            'municipio': forms.Select(attrs={
                'class': 'form-control',
                'widget': Select2Widget
                
            }),
            'estado_ingreso': forms.Select(attrs={
                'class': 'form-control',
                'widget': Select2Widget
                
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción del proyecto'
            }),
            'fecha_inicio': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'fecha_fin': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'fecha_radicacion': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'fecha_revision': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'tipo8': forms.NumberInput(attrs={
                'class': 'InputNumero'
            }),
            'tipo9': forms.NumberInput(attrs={
                'class': 'InputNumero'
            }),
            'tipo10': forms.NumberInput(attrs={
                'class': 'InputNumero'
            }),
            'tipo11': forms.NumberInput(attrs={
                'class': 'InputNumero'
            }),
            'tipo12': forms.NumberInput(attrs={
                'class': 'InputNumero'
            }),
            'tipo14': forms.NumberInput(attrs={
                'class': 'InputNumero'
            }),
            'tipo16': forms.NumberInput(attrs={
                'class': 'InputNumero'
            }),
            'cableoperador': Select2Widget
            
        }