from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Facturacion
# Create your views here.
class FacturacionListView(ListView):
    model = Facturacion
    template_name = 'facturacion/facturacionList.html'
    