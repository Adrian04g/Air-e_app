from django.urls import path
from . import views
# rutas de app
app_name = 'facturacion'

urlpatterns = [
    path('list/', views.FacturacionListView.as_view(), name='lista_facturacion'),
]