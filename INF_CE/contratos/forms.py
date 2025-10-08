from django.forms import modelformset_factory
from django import forms
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
    """Formulario para la creación o edición del contrato principal."""
    class Meta:
        model = Contratos
        # Especifica todos los campos de Contratos que quieres editar/registrar
        fields = [
            'cableoperador', 'tipo_contrato', 
            'estado_contrato', 'duracion_anos', 'inicio_vigencia', 
            'fin_vigencia', 'valor_contrato', 'Garantia', 
            'fecha_radicacion', 'tipo_fecha_radicacion'
        ]
        widgets = {
            'inicio_vigencia': forms.DateInput(attrs={'type': 'date'}),
            'fin_vigencia': forms.DateInput(attrs={'type': 'date'}),
        }
    
    # Añadimos un queryset para limitar las opciones de cableoperadores
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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