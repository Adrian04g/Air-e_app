from django.urls import path
from . import views
# rutas de app
app_name = 'indexapp'

urlpatterns = [
    path('PRST/', views.CableoperadoresListView.as_view(), name='lista_cableoperadores'),
    path('PRST/<int:pk>/', views.cableoperador, name='detalle_cableoperador'),
    path('PRST/crear/', views.CableoperadoreCreateView.as_view(), name='crear_cableoperador'),
]