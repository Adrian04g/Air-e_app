from django import forms
from .models import Asignacion_proyectos
from django.contrib.auth.models import User, Group
from django_select2.forms import Select2Widget
from proyectos.models import Proyectos
# Opciones para el campo de estado del proyecto
SHIFT_CHOICES = [
    ('1', 'En Progreso'),
    ('2', 'Completado'),
]
# Formulario con ModelForms
class AsignacionProyectosForm(forms.ModelForm):
    # Definimos el campo persona_asignada como un ModelChoiceField
    persona_asignada = forms.ModelChoiceField(
        queryset=None, # Lo inicializamos como None, lo filtraremos después
        label="Persona Asignada",
        required=False,
        widget=Select2Widget,
        empty_label="Seleccione una persona"# O "" si quieres que no muestre nada
    )
    nombre_proyecto = forms.ModelChoiceField(
        queryset=Proyectos.objects.all(),
        widget=Select2Widget,
        label="Nombre proyecto",
        empty_label="Seleccione un proyecto" # O "" si quieres que no muestre nada
    )
    nombre_ingeniero = forms.ModelChoiceField(
        queryset=None,  # Lo filtraremos en __init__
        widget=Select2Widget,
        label="Nombre Ingeniero",
        empty_label="Seleccione un ingeniero"
    )
    class Meta:
        model = Asignacion_proyectos
        fields = 'nombre_proyecto','nombre_ingeniero', 'persona_asignada', 'observaciones'
        widgets = {
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción del proyecto'
            }),
            'nombre_proyecto': Select2Widget,
            'persona_asignada': Select2Widget
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filtramos el queryset en la inicialización del formulario
        try:
            # Encuentra el grupo 'Brigadas' o el nombre del grupo que necesites
            grupo_brigadas = Group.objects.get(name='Brigada') 
            # Filtra los usuarios que pertenecen a ese grupo
            self.fields['persona_asignada'].queryset = grupo_brigadas.user_set.all().order_by('username')
        except Group.DoesNotExist:
            # Si el grupo no existe, el queryset queda vacío
            self.fields['persona_asignada'].queryset = User.objects.none()
        # Filtramos el queryset en la inicialización del formulario
        try:
            # Encuentra el grupo 'Brigadas' o el nombre del grupo que necesites
            grupo_brigadas = Group.objects.get(name='admin') 
            # Filtra los usuarios que pertenecen a ese grupo
            self.fields['nombre_ingeniero'].queryset = grupo_brigadas.user_set.all().order_by('username')
        except Group.DoesNotExist:
            # Si el grupo no existe, el queryset queda vacío
            self.fields['nombre_ingeniero'].queryset = User.objects.none()