"""
Views for the SGEE (Sistema de Gestión de Estrategias Educativas) application.
This module contains all the views for handling different aspects of the educational management system.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Static Pages
# ----------------------------------------------------------------------------
def estra_view(request):
    """Render the main strategy page."""
    return render(request, 'pagina_principal.html')

def contact_view(request):
    """Render the contact page."""
    return render(request, 'contactenos.html')

def sobrenos_view(request):
    """Render the about us page."""
    return render(request, 'sobrenos.html')

def visualizarTestimonios(request):
    """Render the testimonials page."""
    return render(request, 'testimonials.html')

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