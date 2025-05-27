from django.shortcuts import render, get_object_or_404, redirect
from estrategias.models import Estrategia
from django.contrib import messages
from django.db.models import Q


def visualizar_estrategias(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar todas las estrategias."""
    query = request.GET.get("q", "")
    estrategias = Estrategia.objects.all()

    # Si el usuario tiene grupo, filtrar por ese grupo
    if hasattr(request.user, 'grupo') and request.user.grupo:
        estrategias = estrategias.filter(grupo=request.user.grupo)

    if query:
        estrategias = estrategias.filter(
            Q(nombre__icontains=query) |
            Q(curso__icontains=query) |
            Q(anio_escolar__icontains=query) |
            Q(grupo__icontains=query) |
            Q(autor__icontains=query)
        )

    return render(request, "usuarios/listar_estrategias.html", {"estrategias": estrategias, "query": query})

def visualizar_estrategia(request, estra_id):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar una estrategia específica."""
    estrategia = get_object_or_404(Estrategia, id=estra_id)
    return render(request, "usuarios/visualizar_estrategia.html", {"estrategia": estrategia})
