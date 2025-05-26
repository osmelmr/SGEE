from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Reporte, Grupo, Estrategia, Evento, Profesor, Encuesta, Usuario
from django.contrib import messages
from data_models.models import Respuesta, Pregunta



def principalG(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Página principal con la lista de grupos."""
    grupos = Grupo.objects.all()
    return render(request, "usuarios/pagina_principal.html", {"grupos": grupos})




def contact_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Render the contact page."""
    return render(request, 'usuarios/contactenos.html')

def sobrenos_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Render the about us page."""
    return render(request, 'usuarios/sobrenos.html')

def visualizarTestimonios(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Render the testimonials page."""
    return render(request, 'usuarios/testimonials.html')


