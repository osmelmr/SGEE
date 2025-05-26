from pyexpat.errors import messages

from django.shortcuts import get_object_or_404, redirect, render

from usuarios.models import Usuario
from django.db.models import Q

def visualizar_usuarios(request):
    """Muestra todos los usuarios con funcionalidad de búsqueda opcional."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    query = request.GET.get('q', '')
    usuarios = Usuario.objects.filter(
        Q(username__icontains=query) |
        Q(cargo__icontains=query) |
        Q(grupo__icontains=query)
    )
    return render(request, 'usuarios/listar_usuarios.html', {
        'usuarios': usuarios,
        'query': query
    })


def visualizar_usuario(request, usuario_id):
    """Muestra los detalles de un usuario específico."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'usuarios/visualizar_usuario.html', {'usuario': usuario})