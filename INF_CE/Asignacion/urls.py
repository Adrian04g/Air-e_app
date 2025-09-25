from django.urls import path
from . import views
from django.contrib.auth.models import User
# rutas de app

app_name = 'asignacion'

urlpatterns = [
    path('asignar/', views.Asignacion_proyectosCreateView.as_view(), name='AsignacionCreate'),
    path('asignado/', views.Asignacion_proyectosListView.as_view(), name='AsignacionList'),
]