from pyexpat.errors import messages
from django.shortcuts import redirect, render


def estra_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para listar grupos.")
        return redirect("p/pagina_principal")
    """Render the main strategy page."""
    return render(request, 'profesor_principal/pagina_principal.html')

def contact_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para listar grupos.")
        return redirect("p/pagina_principal")
    """Render the contact page."""
    return render(request, 'profesor_principal/contactenos.html')

def sobrenos_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para listar grupos.")
        return redirect("p/pagina_principal")
    """Render the about us page."""
    return render(request, 'profesor_principal/sobrenos.html')

def visualizarTestimonios(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para listar grupos.")
        return redirect("p/pagina_principal")
    """Render the testimonials page."""
    return render(request, 'profesor_principal/testimonials.html')

