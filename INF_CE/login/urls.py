from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import inicio_sesion, home_view
# rutas de app
app_name = 'login'
urlpatterns = [
    path('login/', inicio_sesion, name='login'),
    path('logout/', LogoutView.as_view(next_page='login:login'), name='logout'),
    path('', home_view, name='home')
]