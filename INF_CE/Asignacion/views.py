from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from Asignacion.models import Asignacion_proyectos
from Asignacion.forms import AsignacionProyectosForm
from django.views.generic import CreateView
from django.views.generic.list import ListView
# Create your views here.
class Asignacion_proyectosCreateView(CreateView):
    model = Asignacion_proyectos
    form_class = AsignacionProyectosForm
    template_name = 'Asignacion/asignacion_form.html'
    success_url = '/asignacion/asignar/'  # Redirige a una página de éxito después de crear la asignación

class Asignacion_proyectosListView(LoginRequiredMixin,ListView):
    model = Asignacion_proyectos
    template_name = 'Asignacion/Asignacion_proyectosList.html'
    form_class = AsignacionProyectosForm
    
    def get_queryset(self):
        user = self.request.user
        # Verifica si el usuario está en el grupo "Brigada"
        if user.is_superuser:
            return Asignacion_proyectos.objects.all().order_by('-fecha_asignacion')
        elif user.groups.filter(name="Brigada").exists():
            # Filtra por el campo persona_asignada igual al username del usuario
            return Asignacion_proyectos.objects.filter(persona_asignada__username=user.username).order_by('-fecha_asignacion')
        # Si no está en el grupo, retorna queryset vacío o lo que necesites
        return Asignacion_proyectos.objects.none()
