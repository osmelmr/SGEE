from django.shortcuts import render, get_object_or_404, redirect
from profesores.models import  Profesor
from django.contrib import messages
from django.db.models import Q


def visualizar_profesores(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar todos los profesores."""
    query = request.GET.get("q", "")
    if query:
        profesores = Profesor.objects.filter(
            Q(nombre__icontains=query) |
            Q(apellidos__icontains=query) |
            Q(especialidad__icontains=query)
        )
    else:
        profesores = Profesor.objects.all()
    return render(request, "usuarios/listar_profesores.html", {"profesores": profesores, "query": query})

def visualizar_profesor(request, profesor_id):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar un profesor específico."""
    profesor = get_object_or_404(Profesor, id=profesor_id)
    return render(request, "usuarios/visualizar_profesor.html", {"profesor": profesor})
