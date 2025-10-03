from django.shortcuts import render
from django.urls import reverse
from indexapp.forms import CableoperadoresModelForm
from indexapp.models import Cableoperadores
from facturacion.models import Facturacion
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView
# Create your views here.
def admin(request):
    return render(request,'indexapp/admin.html')

# 404
def error(request):
    return render(request, 'error.html')
         
# Clase de cableoperadores
# En tu views.py
class CableoperadoresListView(ListView):
    model = Cableoperadores
    template_name = 'indexapp/cableoperadorList.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        cableoperador_pk = self.request.GET.get('cableoperadorf') # Obtiene el PK del select
        
        if cableoperador_pk and cableoperador_pk != '':
            # 💡 Filtra por la clave primaria (pk)
            queryset = queryset.filter(pk=cableoperador_pk) 
            
        return queryset.order_by('nombre')
    # Continúa en tu views.py, dentro de CableoperadoresListView
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 💡 Pasa la lista de TODOS los cableoperadores para llenar el <select>
        context['cableoperadores'] = Cableoperadores.objects.all().order_by('nombre_largo') 
        return context
    
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
    success_url = '/index/PRST/'
    def form_valid(self, form):
        # 1. Obtener el objeto User logueado
        user = self.request.user

        # 2. Construir el nombre completo (nombre y apellido)
        full_name = f"{user.first_name} {user.last_name}".strip()

        # 3. Asignar el valor al campo 'ejecutiva' de la instancia
        form.instance.ejecutiva = full_name

        # 4. Llamar al método base para guardar el objeto
        return super().form_valid(form)
class CableoperadoresUpdateView(UpdateView):
    model = Cableoperadores
    form_class = CableoperadoresModelForm
    template_name = 'indexapp/CableoperadoresForm.html'
    #success_url = '/index/PRST/'

    def form_valid(self, form):
        # 1. Obtener el objeto User logueado
        user = self.request.user

        # 2. Construir el nombre completo (nombre y apellido)
        full_name = f"{user.first_name} {user.last_name}".strip()

        # 3. Asignar el valor al campo 'ejecutiva' de la instancia
        form.instance.ejecutiva = full_name

        # 4. Llamar al método base para guardar el objeto
        return super().form_valid(form)
    def get_success_url(self):
        # El objeto que se acaba de actualizar está disponible como self.object
        pk = self.object.pk
        
        # Usamos 'reverse' para construir la URL basándonos en el nombre de la ruta
        # y pasamos el pk como argumento de palabra clave (kwargs)
        return reverse('indexapp:detalle_cableoperador', kwargs={'pk': pk})