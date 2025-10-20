from django.urls import path
from . import views
# rutas de app
app_name = 'contratos'

urlpatterns = [
    # URL para crear un nuevo Contrato (y sus recursos)
    path('', views.crear_contrato_con_recursos, name='crear_contrato'),
    # URL de ejemplo para la redirección
    path('lista/', views.lista_contratos, name='lista_contratos'),
    path('<int:pk>/', views.detalle_contrato, name='detalle_contrato'),
    path('lista/<int:pk>/', views.detalle_contrato_elegido, name='detalle_contrato_elegido'),
       # 1. URL para Creación Independiente (Sin PK)
    path('crear/', views.crear_contrato_con_recursos, name='crear_contrato_independiente'),
    
    # 2. URL para Creación Vinculada (Con PK)
    path('crear/<int:pk>/', views.crear_contrato_con_recursos, name='crear_contrato_vinculado'),
    # contratos/urls.py

    # ... otras URLs ...
    path('editar/<int:pk>/', views.actualizar_contrato_con_recursos, name='actualizar_contrato'),

]