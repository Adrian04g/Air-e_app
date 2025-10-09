from django.db import models, transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import inlineformset_factory
from django.urls import reverse # Necesario si usas reverse()
from .models import (
    Contratos,
    Cable, Caja_empalme, Reserva, Nap
)
from contratos.forms import ContratosFormForCableoperador # ⬅️ Asegúrate de importar tu nuevo form
from indexapp.models import Cableoperadores
# Asumo que estos formularios y formsets existen en forms.py
# Nota: La lista de imports del usuario usa CableFormSet, etc., en lugar de CableInlineFormSet.
from .forms import (
    ContratosForm, CableFormSet, CajaEmpalmeFormSet, ReservaFormSet, NapFormSet
)

# Definición de las tuplas de Formset y Nombre de Clase de Recurso
# Utilizamos una lista para iterar fácilmente y aplicar la lógica a todos los recursos.
RESOURCE_FORMSETS_INFO = [
    ('cable', CableFormSet, Cable),
    ('caja', CajaEmpalmeFormSet, Caja_empalme),
    ('reserva', ReservaFormSet, Reserva),
    ('nap', NapFormSet, Nap),
]

# -----------------------------------------------
# 1. VISTA DE CREACIÓN (REGISTRO) - Lógica de guardado robusta
# -----------------------------------------------

"""def crear_contrato_con_recursos(request):
    
    Maneja la creación de un nuevo Contrato y sus registros de recursos 
    (Cable, Caja_empalme, Reserva, Nap) de forma atómica.

    
    form = ContratosForm(request.POST or None)
    
    # 1. Inicializar todos los formsets vacíos para GET o POST fallido (sin instancia aún)
    formsets = {
        name: fs_class(request.POST or None, instance=None, prefix=name)
        for name, fs_class, _ in RESOURCE_FORMSETS_INFO
    }
    
    # Creamos una lista simple para facilitar la validación
    formset_list = list(formsets.values())
    
    if request.method == 'POST':
        
        # 2. Validar todos los formularios y formsets juntos
        if form.is_valid() and all(fs.is_valid() for fs in formset_list):
            
            try:
                # Usamos una transacción atómica para asegurar la consistencia de la base de datos
                with transaction.atomic():
                    
                    # 3. Guardar el objeto Contrato principal
                    contrato = form.save()
                    
                    # 4. Iterar sobre todos los formsets para guardar y/o forzar la creación
                    for name, fs_class, ResourceModel in RESOURCE_FORMSETS_INFO:
                        
                        # Re-inicializamos el formset, esta vez CON la instancia del contrato
                        # y con los datos POST originales.
                        # NOTA: Usamos el mismo prefijo que se usó en la inicialización (name)
                        current_formset = fs_class(request.POST, instance=contrato, prefix=name)
                        
                        # Guardar instancias modificadas (commit=False porque necesitamos asignar el contrato)
                        saved_instances = current_formset.save(commit=False)
                        
                        is_instance_saved = False
                        
                        for instance in saved_instances:
                            # Los formsets inline ya deberían manejar esto, pero forzamos la asignación 
                            # para mayor seguridad en la relación OneToOne.
                            instance.contrato = contrato 
                            instance.save()
                            is_instance_saved = True
                        
                        # LÓGICA CRUCIAL: Si no se guardó ninguna instancia, forzamos la creación.
                        # Esto ocurre si el usuario deja todos los campos de cantidad en blanco/0.
                        if not is_instance_saved:
                            # Crea una instancia de Recurso, vinculada al nuevo contrato.
                            # Los campos de cantidad (tipo8, tipo10, etc.) usarán sus defaults (0).
                            new_resource = ResourceModel(contrato=contrato)
                            new_resource.save()
                            
                    # Éxito: Redirigir a la lista de contratos
                    return redirect('contratos:lista_contratos')

            except Exception as e:
                # Si ocurre un error de base de datos o inesperado
                print(f"Error al guardar la transacción: {e}") 
                # Continúa hacia el renderizado con los datos POST y los errores

    # 5. Contexto para renderizar la plantilla (si es GET o POST fallido)
    context = {
        'form': form,
        'cable_formset': formsets['cable'],
        'caja_empalme_formset': formsets['caja'],
        'reserva_formset': formsets['reserva'],
        'nap_formset': formsets['nap'],
        'titulo': "Registrar Contrato y Usos",
    }
    return render(request, 'contratos/crear_contrato.html', context)"""
# -----------------------------------------------
# VISTA UNIFICADA: SOPORTA CREACIÓN INDIVIDUAL Y VINCULADA
# -----------------------------------------------
def crear_contrato_con_recursos(request, pk=None):
    """
    Maneja la creación de un Contrato.
    Si se proporciona 'pk', el Contrato se vincula automáticamente a ese Cableoperador.
    """
    cableoperador_instance = None
    
    # 1. Determinar el modo de creación y el formulario a usar
    if pk:
        # Modo Vinculado: Obtener el Cableoperador y usar el formulario adaptado
        cableoperador_instance = get_object_or_404(Cableoperadores, pk=pk)
        form_class = ContratosFormForCableoperador
        titulo = f"Registrar Contrato para {cableoperador_instance.nombre}"
    else:
        # Modo Independiente: Usar el formulario completo
        form_class = ContratosForm
        titulo = "Registrar Contrato y Usos (Independiente)"
    
    form = form_class(request.POST or None)
    
    # 2. Inicializar formsets (la lógica es la misma)
    formsets = {
        name: fs_class(request.POST or None, instance=None, prefix=name)
        for name, fs_class, _ in RESOURCE_FORMSETS_INFO
    }
    formset_list = list(formsets.values())
    
    if request.method == 'POST':
        if form.is_valid() and all(fs.is_valid() for fs in formset_list):
            try:
                with transaction.atomic():
                    # 3. Guardar el Contrato (sin commit)
                    contrato = form.save(commit=False)
                    
                    # 4. ASIGNACIÓN CONDICIONAL
                    if cableoperador_instance:
                        contrato.cableoperador = cableoperador_instance # Asignación automática
                    
                    contrato.save()
                    
                    # 5. Guardar Recursos (la lógica es la misma)
                    for name, fs_class, ResourceModel in RESOURCE_FORMSETS_INFO:
                        current_formset = fs_class(request.POST, instance=contrato, prefix=name)
                        saved_instances = current_formset.save(commit=False)
                        is_instance_saved = False
                        
                        for instance in saved_instances:
                            instance.contrato = contrato 
                            instance.save()
                            is_instance_saved = True
                        
                        if not is_instance_saved:
                            new_resource = ResourceModel(contrato=contrato)
                            new_resource.save()
                            
                    # 6. Redirección condicional
                    if cableoperador_instance:
                        # Redirigir al detalle del Cableoperador
                        return redirect('indexapp:detalle_cableoperador', pk=cableoperador_instance.pk)
                    else:
                        # Redirigir a la lista de Contratos (modo independiente)
                        return redirect('contratos:lista_contratos')

            except Exception as e:
                print(f"Error al guardar la transacción: {e}") 
                # Continúa hacia el renderizado con los errores

    # 7. Contexto
    context = {
        'form': form,
        'cableoperador': cableoperador_instance, # Útil para mostrar el nombre
        'cable_formset': formsets['cable'],
        'caja_empalme_formset': formsets['caja'],
        'reserva_formset': formsets['reserva'],
        'nap_formset': formsets['nap'],
        'titulo': titulo,
    }
    return render(request, 'contratos/crear_contrato.html', context)


# -----------------------------------------------
# 2. VISTA DE LECTURA (LISTADO) - EJEMPLO
# -----------------------------------------------

def lista_contratos(request):
    """
    Vista de listado de Contratos.
    Usa select_related() para optimizar la carga del Cableoperador.
    """
    # Consulta optimizada para cargar la información del cableoperador en una sola consulta
    contratos = Contratos.objects.all().select_related('cableoperador')
    return render(request, 'contratos/lista_contratos.html', {'object_list': contratos})


# -----------------------------------------------
# 3. VISTA DE LECTURA (DETALLE) - RECOMENDADA
# -----------------------------------------------

def detalle_contrato(request, pk):
    """
    Vista de detalle para un Contrato, mostrando toda su información y recursos asociados.
    """
    # Consulta optimizada para cargar el Contrato y todos sus recursos en una sola consulta
    contrato = get_object_or_404(
        Contratos.objects.select_related(
            'cable',           # Acceso directo al OneToOneField Cable
            'caja_empalme',    # Acceso directo a Caja_empalme
            'reserva',         # Acceso directo a Reserva
            'nap',             # Acceso directo a Nap
            'cableoperador'    # Acceso a Cableoperadores
        ), 
        pk=pk
    )

    context = {
        'contrato': contrato,
        'titulo': f"Detalle del Contrato {contrato.pk}",
        'p': ''
    }
    return render(request, 'contratos/detalle_contrato.html', context)