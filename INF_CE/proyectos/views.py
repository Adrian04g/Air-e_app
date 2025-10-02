from django.shortcuts import render
from .forms import ProyectosModelForm
from .models import Proyectos
from django.views.generic import CreateView, ListView
# Create your views here.
# vista del formulario de Proyectos
class ProyectosCreateView(CreateView):
    model = Proyectos
    form_class = ProyectosModelForm
    template_name = 'proyectos/ProyectosForm.html'
    success_url = 'proyectos/ProyectosForm.html'
    def form_valid(self, form):
        # 1. Obtener el objeto User logueado
        user = self.request.user

        # 2. Construir el nombre completo (nombre y apellido)
        full_name = f"{user.first_name} {user.last_name}".strip()

        # 3. Asignar el valor al campo 'responsable' de la instancia
        form.instance.responsable = full_name
        
        # 4. Llamar al método base para guardar el objeto
        return super().form_valid(form)
    
# vista para listar los proyectos
class ProyectosListView(ListView):
    model = Proyectos
    template_name = 'proyectos/ProyectosList.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        cableoperador = self.request.GET.get('cableoperadorf')
        if cableoperador:
            queryset = queryset.filter(cableoperador__nombre=cableoperador)
        return queryset.order_by('-fecha_radicacion')