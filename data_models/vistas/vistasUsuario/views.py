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
        nombre = request.POST.get('nombre')
        primer_apellido = request.POST.get('primer-apellido')
        segundo_apellido = request.POST.get('segundo-apellido')
        sexo = request.POST.get('sexo')
        grupo = request.POST.get('grupo')
        solapin = request.POST.get('solapin')
        cargo = request.POST.get('cargo')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        username = request.POST.get('user')
        password = request.POST.get('password')

        # Validar si el usuario ya existe
        if Usuario.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
        elif Usuario.objects.filter(solapin=solapin).exists():
            messages.error(request, 'El solapín ya está registrado.')
        elif Usuario.objects.filter(email=correo).exists():
            messages.error(request, 'El correo ya está registrado.')
        else:
            # Crear el usuario
            usuario = Usuario.objects.create_user(
                username=username,
                password=password,
                first_name=nombre,
                last_name=primer_apellido,
                email=correo,
                cargo=cargo,
                sexo=sexo,
                grupo=grupo,
                solapin=solapin,
                telefono=telefono
            )
            # Guardar el segundo apellido si se proporciona
            usuario.last_name = f"{primer_apellido} {segundo_apellido}" if segundo_apellido else primer_apellido
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
    return redirect('profesor_principal/visualizar__usuarios')

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
        usuario.username = request.POST.get('username', usuario.username)
        usuario.cargo = request.POST.get('cargo', usuario.cargo)
        usuario.sexo = request.POST.get('sexo', usuario.sexo)
        usuario.grupo = request.POST.get('grupo', usuario.grupo)
        usuario.solapin = request.POST.get('solapin', usuario.solapin)
        usuario.telefono = request.POST.get('telefono', usuario.telefono)
        usuario.save()
        messages.success(request, f'Usuario {usuario.username} modificado exitosamente.')
        return redirect('profesor_principal/visualizar__usuarios')

    return render(request, 'modificar_usuario.html', {'usuario': usuario})

# Visualizar un usuario específico
def visualizarUsuario(request, usuario_id):
    """Muestra los detalles de un usuario específico."""
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'profesor_principal/visualizar__usuario.html', {'usuario': usuario})