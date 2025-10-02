from django.shortcuts import render
from indexapp.forms import CableoperadoresModelForm
from indexapp.models import Cableoperadores
from facturacion.models import Facturacion
from django.views.generic import CreateView
from django.views.generic.list import ListView
# Create your views here.
def admin(request):
    return render(request,'indexapp/admin.html')

# 404
def error(request):
    return render(request, 'error.html')
         
# Clase de cableoperadores
class CableoperadoresListView(ListView):
    model = Cableoperadores
    template_name = 'indexapp/cableoperadorList.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        cableoperador = self.request.GET.get('cableoperadorf')
        if cableoperador:
            queryset = queryset.filter(nombre=cableoperador)
        return queryset.order_by('nombre')
    
def cableoperador(request, pk=None):
    if pk:
        cableoperador = Cableoperadores.objects.get(pk=pk)
        facturas = Facturacion.objects.filter(Nombre_prst=cableoperador).order_by('-Fecha_fact')
        object = {
            'object': cableoperador,
            'facturas': facturas    
        }
        return render(request, 'indexapp/cableoperador.html', object)

class CableoperadoreCreateView(CreateView):
    model = Cableoperadores
    form_class = CableoperadoresModelForm
    template_name = 'indexapp/CableoperadoresForm.html'
    success_url = '/index/CableoperadoresForm.html'
