"""
Views for the SGEE (Sistema de Gestión de Estrategias Educativas) application.
This module contains all the views for handling different aspects of the educational management system.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Static Pages
# ----------------------------------------------------------------------------


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.es_profesor():
                return redirect('pagina_principal')
            return redirect('pagina_principal_g')  # Redirige a la página principal después del login
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')


def logout_view(request):
    """
    Cierra la sesión del usuario y redirige a la página de login.
    """
    logout(request)
    return redirect('login')