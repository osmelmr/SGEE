from django.shortcuts import render, get_object_or_404, redirect
from estrategias.models import Estrategia
from django.contrib import messages
from django.db.models import Q


def visualizarEstrategias(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar todas las estrategias."""
    query = request.GET.get("q", "")
    if query:
        estrategias = Estrategia.objects.filter(
            Q(nombre__icontains=query) |
            Q(curso__icontains=query) |
            Q(anio_escolar__icontains=query) |
            Q(grupo__nombre__icontains=query) |
            Q(autor__icontains=query)
        )
    else:
        estrategias = Estrategia.objects.all()
    return render(request, "usuarios/listar_estrategias.html", {"estrategias": estrategias, "query": query})

def visualizarEstrategia(request, estrategia_id):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar una estrategia específica."""
    estrategia = get_object_or_404(Estrategia, id=estrategia_id)
    return render(request, "usuarios/visualizar_estrategia.html", {"estrategia": estrategia})
