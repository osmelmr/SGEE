from django.shortcuts import render, get_object_or_404, redirect
from reportes.models import Reporte
from django.contrib import messages
from django.db.models import Q

def visualizar_reportes(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar todos los reportes."""
    query = request.GET.get("q", "")
    if query:
        reportes = Reporte.objects.filter(
            Q(titulo__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(autor__icontains=query)
        )
    else:
        reportes = Reporte.objects.all()
    return render(request, "usuarios/listar_reportes.html", {"reportes": reportes, "query": query})

def visualizar_reporte(request, reporte_id):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar un reporte específico."""
    reporte = get_object_or_404(Reporte, id=reporte_id)
    return render(request, "usuarios/visualizar_reporte.html", {"reporte": reporte})
