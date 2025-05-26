from pyexpat.errors import messages
from django.shortcuts import redirect, render


def estra_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    
    """Render the main strategy page."""
    return render(request, 'usuarios/pagina_principal.html')

def contact_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    
    """Render the contact page."""
    return render(request, 'usuarios/contactenos.html')

def sobrenos_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    
    """Render the about us page."""
    return render(request, 'usuarios/sobrenos.html')

def visualizarTestimonios(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    
    """Render the testimonials page."""
    return render(request, 'usuarios/testimonials.html')

