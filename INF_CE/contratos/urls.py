from django.urls import path
from . import views
# rutas de app
app_name = 'contratos'

urlpatterns = [
    # URL para crear un nuevo Contrato (y sus recursos)
    path('', views.crear_contrato_con_recursos, name='crear_contrato'),
    # URL de ejemplo para la redirección
    path('lista/', views.lista_contratos, name='lista_contratos'),
    path('<int:pk>/', views.detalle_contrato, name='detalle_contrato')
]