from pyexpat.errors import messages

from django.shortcuts import redirect, render

from grupos.models import Grupo
from django.db.models import Q

def visualizar_grupo(request, grupo_id):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    grupo = Grupo.objects.get(id=grupo_id)
    return render(request, 'profesor_principal/visualizar_grupo.html', {'grupo': grupo})


def visualizar_grupos(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    query = request.GET.get('q', '')
    if query:
        grupos = Grupo.objects.filter(
            Q(nombre__icontains=query) |
            Q(direccion__icontains=query) |
            Q(curso__icontains=query) |
            Q(anio_escolar__icontains=query) |
            Q(caracterizacion__icontains=query)
        )
    else:
        grupos = Grupo.objects.all()
    return render(request, 'usuarios/listar_grupos.html', {'grupos': grupos, 'query': query})