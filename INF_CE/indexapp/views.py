from django.shortcuts import render
from indexapp.forms import ProyectosModelForm
from indexapp.models import Proyectos
from django.views.generic import CreateView
from django.views.generic.list import ListView
# Create your views here.
def admin(request):
    return render(request,'indexapp/admin.html')

# vista para listar los proyectos
class ProyectosListView(ListView):
    model = Proyectos
    template_name = 'indexapp/ProyectosList.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        cableoperador = self.request.GET.get('cableoperadorf')
        if cableoperador:
            queryset = queryset.filter(cableoperador__nombre=cableoperador)
        return queryset.order_by('-fecha_radicacion')
    


# 404
def error(request):
    return render(request, 'error.html')

# vista del formulario de Proyectos
class ProyectosCreateView(CreateView):
    model = Proyectos
    form_class = ProyectosModelForm
    template_name = 'indexapp/ProyectosForm.html'
    success_url = '/index/crear/'

            

    
