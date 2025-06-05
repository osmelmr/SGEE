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
        # Usar los nombres de campo personalizados para evitar autocompletado/sugerencias
        username = request.POST.get('user_login')
        password = request.POST.get('pass_login')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(request.user, 'es_profesor') and request.user.es_profesor():
                return redirect('p_pagina_principal')
            return redirect('pagina_principal')
        else:
            messages.error(request, 'Usuario incorrecto/Clave no valida.')
    return render(request, 'login.html')


def logout_view(request):
    """
    Cierra la sesión del usuario y redirige a la página de login.
    """
    logout(request)
    return redirect('login')