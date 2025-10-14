from django.forms import modelformset_factory
from django import forms
from django_select2.forms import Select2Widget
# Importamos todos los modelos relevantes del archivo models.py
from .models import (
    Contratos, 
    Cableoperadores, 
    Cable, 
    Caja_empalme, 
    Reserva, 
    Nap
)
# -------------------------
# 1. Formulario Principal (Contratos)
# -------------------------
class ContratosForm(forms.ModelForm):
    # Formulario para la creación o edición del contrato principal.
    class Meta:
        model = Contratos
        # Especifica todos los campos de Contratos que quieres editar/registrar
        fields = [
            'tipo_contrato', 'cableoperador',
            'estado_contrato', 'duracion_anos', 'inicio_vigencia', 
            'fin_vigencia', 'valor_contrato',
            'fecha_radicacion', 'tipo_fecha_radicacion',
            'vigencia_amparo_poliza_cumplimiento', 'inicio_vigencia_poliza_cumplimiento',
            'fin_vigencia_poliza_cumplimiento', 'expedicion_poliza_cumplimiento',
            'monto_asegurado_poliza_cumplimiento', 'valor_monto_asegurado_poliza_cumplimiento',
            'valor_asegurado_poliza_cumplimiento', 'numero_poliza_cumplimiento',
            'inicio_amparo_poliza_cumplimiento', 'fin_amparo_poliza_cumplimiento',
            'expedicion_poliza_cumplimiento', 'vigencia_amparo_poliza_rce',
            'inicio_vigencia_poliza_rce', 'fin_vigencia_poliza_rce',
            'expedicion_poliza_rce', 'monto_asegurado_poliza_rce',
            'valor_monto_asegurado_poliza_rce',
            'valor_asegurado_poliza_rce',
            'numero_poliza_rce', 'inicio_amparo_poliza_rce',
            'fin_amparo_poliza_rce', 'expedicion_poliza_rce',
            'tomador', 'aseguradora'
            
        ]
        widgets = {
            'inicio_vigencia': forms.DateInput(attrs={ 'type': 'date',
                'class': 'form-control',
                'placeholder': 'Inicio de Vigencia'}),
            'fin_vigencia': forms.DateInput(attrs={'type': 'date'}),
            'tipo_contrato' : forms.Select(attrs={'class': 'form-control'}),
            'duracion_anos' : forms.NumberInput(attrs={'class': 'InputNumero'}),
            # Campos de la Póliza de Cumplimiento
            'inicio_vigencia_poliza_cumplimiento' : forms.DateInput(attrs={'type': 'date'}),
            'fin_vigencia_poliza_cumplimiento' : forms.DateInput(attrs={'type': 'date'}),
            'inicio_amparo_poliza_cumplimiento' : forms.DateInput(attrs={'type': 'date'}),
            'fin_amparo_poliza_cumplimiento' : forms.DateInput(attrs={'type': 'date'}),
            'expedicion_poliza_cumplimiento' : forms.DateInput(attrs={'type': 'date'}),
            'numero_poliza_cumplimiento' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar numero de Póliza'}),
            'vigencia_amparo_poliza_cumplimiento' : forms.Select(attrs={'class': 'form-control'}),
            'valor_asegurado_poliza_cumplimiento' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar valor asegurado'}),
            'valor_monto_asegurado_poliza_cumplimiento' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar valor monto asegurado'}),
            # Campos de la Póliza de RCE
            'inicio_vigencia_poliza_rce' : forms.DateInput(attrs={'type': 'date'}),
            'fin_vigencia_poliza_rce' : forms.DateInput(attrs={'type': 'date'}),
            'inicio_amparo_poliza_rce' : forms.DateInput(attrs={'type': 'date'}),
            'fin_amparo_poliza_rce' : forms.DateInput(attrs={'type': 'date'}),
            'expedicion_poliza_rce' : forms.DateInput(attrs={'type': 'date'}),
            'numero_poliza_rce' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar numero de Póliza'}),
            'vigencia_amparo_poliza_rce' : forms.Select(attrs={'class': 'form-control'}),
            'valor_asegurado_poliza_rce' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar valor asegurado'}),
            'valor_monto_asegurado_poliza_rce' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar valor monto asegurado'}),
            'tomador' : forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ingresar tomador'}),
            'aseguradora' : forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ingresar aseguradora'}),
            'fecha_radicacion' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numero de Radicación'}),
            'tipo_fecha_radicacion' : forms.Select(attrs={'class': 'form-control'})
        }
    
    # Añadimos un queryset para limitar las opciones de cableoperadores
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cableoperador'].queryset = Cableoperadores.objects.all().order_by('nombre')
        # Puedes añadir clases de CSS aquí para mejor estilo
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-input w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'})
# -------------------------
# 1. Formulario contrato individual
# -------------------------
class ContratosFormForCableoperador(forms.ModelForm):
    """Formulario para la creación o edición del contrato principal."""
    class Meta:
        model = Contratos
        # Especifica todos los campos de Contratos que quieres editar/registrar
        fields = [
            'tipo_contrato', 
            'estado_contrato', 'duracion_anos', 'inicio_vigencia', 
            'fin_vigencia', 'valor_contrato',
            'fecha_radicacion', 'tipo_fecha_radicacion', 
            # Campos de la Póliza de Cumplimiento
            'numero_poliza_cumplimiento',
            'vigencia_amparo_poliza_cumplimiento', 'inicio_vigencia_poliza_cumplimiento',
            'fin_vigencia_poliza_cumplimiento', 'expedicion_poliza_cumplimiento',
            'monto_asegurado_poliza_cumplimiento', 'valor_monto_asegurado_poliza_cumplimiento',
             'inicio_amparo_poliza_cumplimiento',
            'fin_amparo_poliza_cumplimiento',
            # Campos de la Póliza de RCE
            'numero_poliza_rce',
            'vigencia_amparo_poliza_rce', 'inicio_vigencia_poliza_rce',
            'fin_vigencia_poliza_rce', 'expedicion_poliza_rce',
            'monto_asegurado_poliza_rce', 'valor_monto_asegurado_poliza_rce',
            'inicio_amparo_poliza_rce',
            'fin_amparo_poliza_rce', 'expedicion_poliza_rce',
            'tomador', 'aseguradora'
        ]
        widgets = {
            'inicio_vigencia': forms.DateInput(attrs={ 'type': 'date',
                'class': 'form-control',
                'placeholder': 'Inicio de Vigencia'}),
            'fin_vigencia': forms.DateInput(attrs={'type': 'date'}),
            'tipo_contrato' : forms.Select(attrs={'class': 'form-control'}),
            'duracion_anos' : forms.NumberInput(attrs={'class': 'InputNumero'}),
            # Campos de la Póliza de Cumplimiento
            'inicio_vigencia_poliza_cumplimiento' : forms.DateInput(attrs={'type': 'date'}),
            'fin_vigencia_poliza_cumplimiento' : forms.DateInput(attrs={'type': 'date'}),
            'inicio_amparo_poliza_cumplimiento' : forms.DateInput(attrs={'type': 'date'}),
            'fin_amparo_poliza_cumplimiento' : forms.DateInput(attrs={'type': 'date'}),
            'expedicion_poliza_cumplimiento' : forms.DateInput(attrs={'type': 'date'}),
            'numero_poliza_cumplimiento' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar numero de Póliza'}),
            'vigencia_amparo_poliza_cumplimiento' : forms.Select(attrs={'class': 'form-control'}),
            'valor_asegurado_poliza_cumplimiento' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar valor asegurado'}),
            'valor_monto_asegurado_poliza_cumplimiento' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar valor monto asegurado'}),
            # Campos de la Póliza de RCE
            'inicio_vigencia_poliza_rce' : forms.DateInput(attrs={'type': 'date'}),
            'fin_vigencia_poliza_rce' : forms.DateInput(attrs={'type': 'date'}),
            'inicio_amparo_poliza_rce' : forms.DateInput(attrs={'type': 'date'}),
            'fin_amparo_poliza_rce' : forms.DateInput(attrs={'type': 'date'}),
            'expedicion_poliza_rce' : forms.DateInput(attrs={'type': 'date'}),
            'numero_poliza_rce' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar numero de Póliza'}),
            'vigencia_amparo_poliza_rce' : forms.Select(attrs={'class': 'form-control'}),
            'valor_asegurado_poliza_rce' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar valor asegurado'}),
            'valor_monto_asegurado_poliza_rce' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar valor monto asegurado'}),
            'tomador' : forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ingresar tomador'}),
            'aseguradora' : forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ingresar aseguradora'}),
            'fecha_radicacion' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numero de Radicación'}),
            'tipo_fecha_radicacion' : forms.Select(attrs={'class': 'form-control'})
        }
    
    # Añadimos un queryset para limitar las opciones de cableoperadores
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'cableoperador' in self.fields:
            # Esta lógica SOLO se ejecuta si el campo está presente (Modo Independiente).
            self.fields['cableoperador'].queryset = Cableoperadores.objects.all().order_by('nombre')
        # Puedes añadir clases de CSS aquí para mejor estilo
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-input w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'})
# -------------------------
# 2. Formsets para Recursos (Relaciones Uno a Uno)
# -------------------------

# Usamos forms.inlineformset_factory para las relaciones 1 a 1 inversas.
# Como la relación es 1 a 1, max_num=1 y extra=0 aseguran que solo se pueda 
# crear UN registro de recurso por contrato.

# Formulario para Cable
CableFormSet = forms.inlineformset_factory(
    Contratos, Cable, 
    fields='__all__', 
    extra=1, 
    max_num=1,
    can_delete=False
)

# Formulario para Caja_empalme
CajaEmpalmeFormSet = forms.inlineformset_factory(
    Contratos, Caja_empalme, 
    fields='__all__', 
    extra=1, 
    max_num=1,
    can_delete=False
)

# Formulario para Reserva
ReservaFormSet = forms.inlineformset_factory(
    Contratos, Reserva, 
    fields='__all__', 
    extra=1, 
    max_num=1,
    can_delete=False
)

# Formulario para Nap
NapFormSet = forms.inlineformset_factory(
    Contratos, Nap, 
    fields='__all__', 
    extra=1, 
    max_num=1,
    can_delete=False
)