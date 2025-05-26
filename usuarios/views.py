from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from data_models.models import Usuario

# Visualizar todos los usuarios
def visualizarUsuarios(request):
    """Muestra todos los usuarios con funcionalidad de búsqueda opcional."""
    query = request.GET.get('q', '')
    usuarios = Usuario.objects.filter(
        Q(username__icontains=query) |
        Q(cargo__icontains=query) |
        Q(grupo__icontains=query)
    )
    return render(request, 'profesor_principal/listar_usuarios.html', {
        'usuarios': usuarios,
        'query': query
    })

# Crear un nuevo usuario
def crearUsuario(request):
    """Crea un nuevo usuario."""
    if request.method == 'POST':
        # Obtener los datos del formulario
        form_data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'second_last_name': request.POST.get('second_last_name'),
            'sexo': request.POST.get('sexo'),
            'grupo': request.POST.get('grupo'),
            'solapin': request.POST.get('solapin'),
            'cargo': request.POST.get('cargo'),
            'telefono': request.POST.get('telefono'),
            'email': request.POST.get('email'),
            'username': request.POST.get('username'),
            'password': request.POST.get('password')
        }

        # Validar si el usuario ya existe
        if Usuario.objects.filter(username=form_data['username']).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
        elif Usuario.objects.filter(solapin=form_data['solapin']).exists():
            messages.error(request, 'El solapín ya está registrado.')
        elif Usuario.objects.filter(email=form_data['email']).exists():
            messages.error(request, 'El correo ya está registrado.')
        else:
            # Crear el usuario
            usuario = Usuario.objects.create_user(
                username=form_data['username'],
                password=form_data['password'],
                first_name=form_data['first_name'],
                last_name=form_data['last_name'],
                email=form_data['email'],
                cargo=form_data['cargo'],
                sexo=form_data['sexo'],
                grupo=form_data['grupo'],
                solapin=form_data['solapin'],
                telefono=form_data['telefono']
            )
            # Guardar el segundo apellido si se proporciona
            if form_data['second_last_name']:
                usuario.last_name = f"{form_data['last_name']} {form_data['second_last_name']}"
            usuario.save()

            messages.success(request, f'Usuario {usuario.username} creado exitosamente.')
            return redirect('usuarios')  # Redirige a la lista de usuarios

    return render(request, 'profesor_principal/formular_usuario.html')

# Eliminar un usuario específico
def eliminarUsuario(request, usuario_id):
    """Elimina un usuario específico."""
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    messages.success(request, f'Usuario {usuario.username} eliminado exitosamente.')
    return redirect('usuarios')

# Eliminar múltiples usuarios
def eliminarUsuarios(request):
    """Elimina múltiples usuarios seleccionados."""
    if request.method == 'POST':
        ids = request.POST.getlist('ids')
        Usuario.objects.filter(id__in=ids).delete()
        messages.success(request, 'Usuarios eliminados exitosamente.')
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Modificar un usuario existente
def modificarUsuario(request, usuario_id):
    """Modifica un usuario existente."""
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form_data = {
            'username': request.POST.get('username', usuario.username),
            'cargo': request.POST.get('cargo', usuario.cargo),
            'sexo': request.POST.get('sexo', usuario.sexo),
            'grupo': request.POST.get('grupo', usuario.grupo),
            'solapin': request.POST.get('solapin', usuario.solapin),
            'telefono': request.POST.get('telefono', usuario.telefono)
        }

        try:
            for key, value in form_data.items():
                setattr(usuario, key, value)
            usuario.save()
            messages.success(request, f'Usuario {usuario.username} modificado exitosamente.')
            return redirect('usuarios')
        except Exception as e:
            messages.error(request, f'Error al modificar el usuario: {str(e)}')

    return render(request, 'modificar_usuario.html', {'usuario': usuario})

# Visualizar un usuario específico
def visualizarUsuario(request, usuario_id):
    """Muestra los detalles de un usuario específico."""
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'profesor_principal/visualizar__usuario.html', {'usuario': usuario})