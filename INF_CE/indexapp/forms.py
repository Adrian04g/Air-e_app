from django import forms
from .models import Proyectos, Cableoperadores
from django.contrib.auth.models import User, Group
from django_select2.forms import Select2Widget
# Opciones para el campo de estado del proyecto
SHIFT_CHOICES = [
    ('1', 'En Progreso'),
    ('2', 'Completado'),
    ('3', 'Pendiente'),
]


# Formulario con ModelForms
class ProyectosModelForm(forms.ModelForm):
    responsable = forms.ModelChoiceField(
        queryset=None,  # Lo filtraremos en __init__
        widget=Select2Widget,
        empty_label="Seleccione un responsable",
        label="Ejecutiva responsable"
    )
    class Meta:
        model = Proyectos
        fields = '__all__'
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            grupo_brigadas = Group.objects.get(name='Ejecutivas')
            self.fields['responsable'].queryset = grupo_brigadas.user_set.all().order_by('username')
        except Group.DoesNotExist:
            self.fields['responsable'].queryset = User.objects.none()

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
        
        