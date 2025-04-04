from django.shortcuts import render, get_object_or_404, redirect
# from data_models.models import Usuario
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

def visualizarUsuarios(request):
    """Display all strategies with optional search functionality."""
    query = request.GET.get('q', '')
    
    return render(request, 'usuarios.html', {
        'query': query
    })

# Form Views
# ----------------------------------------------------------------------------
def crearUsuario(request):
    return render(request, 'formulario_usuario.html')

# Delete Views - Single Item
# ----------------------------------------------------------------------------
def eliminarUsuario(request, estra_id):
    
    return redirect('usuarios')

# Delete Views - Multiple Items
# ----------------------------------------------------------------------------
def eliminarUsuarios(request):
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def modificarUsuario(request, estra_id):
    
    return render(request, 'modificar_usuario.html')

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def visualizarUsuario(request, estra_id):
    """View a single strategy."""
    
    return render(request, 'visualizar_usuario.html')