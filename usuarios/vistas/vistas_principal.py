from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from usuarios.models import Usuario
from grupos.models import Grupo  # Asegúrate de tener este import

# Visualizar todos los usuarios
def visualizar_usuarios(request):
    """Muestra todos los usuarios con funcionalidad de búsqueda opcional."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    query = request.GET.get('q', '')
    usuarios = Usuario.objects.filter(
        Q(username__icontains=query) |
        Q(rol__icontains=query) |
        Q(grupo__icontains=query)
    )
    return render(request, 'profesor_principal/listar_usuarios.html', {
        'usuarios': usuarios,
        'query': query
    })

# Crear un nuevo usuario
def crear_usuario(request):
    """Crea un nuevo usuario.
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    """
    grupos = Grupo.objects.all()
    if request.method == 'POST':
        # Obtener los datos del formulario
        form_data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'second_last_name': request.POST.get('second_last_name'),
            'sexo': request.POST.get('sexo'),
            'grupo': request.POST.get('grupo'),
            'solapin': request.POST.get('solapin'),
            'rol': request.POST.get('rol'),
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
        elif Usuario.objects.filter(telefono=form_data['telefono']).exists():
            messages.error(request, 'El telefono ya está registrado.')
        else:
            # Crear el usuario
            usuario = Usuario.objects.create_user(
                username=form_data['username'],
                password=form_data['password'],
                first_name=form_data['first_name'],
                last_name=form_data['last_name'],
                second_last_name=form_data['second_last_name'],
                email=form_data['email'],
                rol=form_data['rol'],
                sexo=form_data['sexo'],
                grupo=form_data['grupo'],
                solapin=form_data['solapin'],
                telefono=form_data['telefono']
            )
            # Guardar el segundo apellido si se proporciona
            usuario.save()

            messages.success(request, "Registro satisfactorio.")
            return redirect('p_usuarios')  # Redirige a la lista de usuarios

    return render(request, 'profesor_principal/formular_usuario.html', {'grupos': grupos})

# Eliminar un usuario específico
def eliminar_usuario(request, usuario_id):
    """Elimina un usuario específico."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    messages.success(request, "Eliminación satisfactoria.")
    return redirect('p_usuarios')

# Eliminar múltiples usuarios
def eliminar_usuarios(request):
    """Elimina múltiples usuarios seleccionados."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    if request.method == 'POST':
        ids = request.POST.getlist('ids')
        Usuario.objects.filter(id__in=ids).delete()
        messages.success(request, "Eliminación satisfactoria.")
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Modificar un usuario existente
def modificar_usuario(request, usuario_id):
    """Modifica un usuario existente."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    usuario = get_object_or_404(Usuario, id=usuario_id)
    grupos = Grupo.objects.all()
    if request.method == 'POST':
        form_data = {
            'username': request.POST.get('username', usuario.username),
            'rol': request.POST.get('rol', usuario.rol),
            'sexo': request.POST.get('sexo', usuario.sexo),
            'grupo': request.POST.get('grupo', usuario.grupo),
            'solapin': request.POST.get('solapin', usuario.solapin),
            'telefono': request.POST.get('telefono', usuario.telefono),
            'second_last_name': request.POST.get('second_last_name', usuario.second_last_name),
            'email': request.POST.get('email', usuario.email),
            'first_name': request.POST.get('first_name', usuario.first_name),
            'last_name': request.POST.get('last_name', usuario.last_name),
            'password': request.POST.get('password', None),  # Añadido
        }

        try:
            for key, value in form_data.items():
                if key == 'password':
                    if value:  # Solo si se proporciona una nueva contraseña
                        usuario.set_password(value)
                else:
                    setattr(usuario, key, value)
            usuario.save()
            messages.success(request, "Modificación satisfactoria.")
            return redirect('p_usuarios')
        except Exception as e:
            messages.error(request, f'Error al modificar el usuario: {str(e)}')

    return render(request, 'profesor_principal/modificar_usuario.html', {'usuario': usuario, 'grupos': grupos})


# Visualizar un usuario específico
def visualizar_usuario(request, usuario_id):
    """Muestra los detalles de un usuario específico."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'profesor_principal/visualizar_usuario.html', {'usuario': usuario})