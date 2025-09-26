from django.urls import path
from . import views
# rutas de app
app_name = 'indexapp'

urlpatterns = [
    path('crear/', views.ProyectosCreateView.as_view(), name='crear_proyecto'),
    path('list/', views.ProyectosListView.as_view(), name='lista_proyectos'),
    path('PRST/', views.CableoperadoresListView.as_view(), name='lista_cableoperadores'),
    path('PRST/<int:pk>/', views.cableoperador, name='detalle_cableoperador'),
]