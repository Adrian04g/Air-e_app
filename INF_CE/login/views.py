# login/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from login.forms import LoginForm
from django.contrib.auth.decorators import login_required

# Script para validar que el formulario de inicio de sesión funcione
def inicio_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', 'login:home'))
            else:
                form.add_error(None, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = LoginForm()
    return render(request, 'login/inicio.html', {'form': form})

# Funcion para que el usuario pueda acceder a la vista de inicio
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login:login')
    return render(request, 'login/home.html')