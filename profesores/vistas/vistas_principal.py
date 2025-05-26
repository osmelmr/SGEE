from django.shortcuts import render, get_object_or_404, redirect
from profesores.models import Profesor
from grupos.models import Grupo
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

def visualizarProfesores(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    query = request.GET.get('q', '')
    if query:
        profesores = Profesor.objects.filter(
            Q(nombre__icontains=query) |
            Q(primer_apellido__icontains=query) |
            Q(segundo_apellido__icontains=query) |
            Q(sexo__icontains=query) |
            Q(categoria_docente__icontains=query) |
            Q(asignatura__icontains=query) |
            Q(solapin__icontains=query) |
            Q(telefono__icontains=query) |
            Q(correo__icontains=query) |
            Q(descripcion__icontains=query)
        )
    else:
        profesores = Profesor.objects.all()
    return render(request, 'profesor_principal/listar_profesores.html', {
        'profesores': profesores,
        'query': query
    })

def crearProfesor(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    grupos = Grupo.objects.all()

    if request.method == 'POST':
        form_data = {
            'nombre': request.POST.get('nombre'),
            'primer_apellido': request.POST.get('primer_apellido'),
            'segundo_apellido': request.POST.get('segundo_apellido'),
            'sexo': request.POST.get('sexo'),
            'categoria_docente': request.POST.get('categoria_docente'),
            'asignatura': request.POST.get('asignatura'),
            'solapin': request.POST.get('solapin'),
            'telefono': request.POST.get('telefono'),
            'correo': request.POST.get('correo'),
            'descripcion': request.POST.get('descripcion'),
        }
        grupos_ids = request.POST.getlist('grupos')  # Obtén los IDs seleccionados
        grupo_asignado_id = request.POST.get('grupo_asignado')  # Obtén el grupo asignado

        # Validar campos obligatorios
        if not all(form_data.values()):
            messages.error(request, "Todos los campos obligatorios deben ser completados.")
            return render(request, 'profesor_principal/formular_profesor.html', {'grupos': grupos})

        try:
            # Crear el profesor
            profesor = Profesor.objects.create(**form_data)
            profesor.grupos.set(grupos_ids)  # Asignar grupos al profesor

            # Asignar el profesor como guía del grupo
            if grupo_asignado_id:
                grupo_asignado = Grupo.objects.get(id=grupo_asignado_id)
                grupo_asignado.guia = profesor
                grupo_asignado.save()

            messages.success(request, "Profesor registrado correctamente.")
            return redirect('p_profesores')
        except Exception as e:
            print(f"Error: {str(e)}")
            messages.error(request, f"Error al registrar el profesor: {str(e)}")

    return render(request, 'profesor_principal/formular_profesor.html', {'grupos': grupos})

def eliminarProfesor(request, profesor_id):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    """Delete a single professor."""
    profesor = get_object_or_404(Profesor, id=profesor_id)
    profesor.delete()
    messages.success(request, "Profesor eliminado correctamente.")
    return redirect('p_profesores')

def eliminarProfesores(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    """Delete multiple strategies."""
    if request.method == 'POST':
        profesores_ids = request.POST.getlist('profesores[]')
        if profesores_ids:
            Profesor.objects.filter(id__in=profesores_ids).delete()
            messages.success(request, "Profesores eliminadas correctamente.")
        else:
            messages.error(request, "No se seleccionaron profesores para eliminar.")
        return redirect('p_profesores')
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def modificarProfesor(request, profesor_id):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    """Modify a single professor."""
    profesor = get_object_or_404(Profesor, id=profesor_id)
    
    if request.method == 'POST':
        form_data = {
            'nombre': request.POST.get('nombre'),
            'primer_apellido': request.POST.get('primer_apellido'),
            'segundo_apellido': request.POST.get('segundo_apellido'),
            'sexo': request.POST.get('sexo'),
            'categoria_docente': request.POST.get('categoria_docente'),
            'asignatura': request.POST.get('asignatura'),
            'solapin': request.POST.get('solapin'),
            'telefono': request.POST.get('telefono'),
            'correo': request.POST.get('correo'),
            'descripcion': request.POST.get('descripcion')
        }

        # Validate required fields
        if not all(form_data.values()):
            messages.error(request, "Todos los campos obligatorios deben ser completados.")
            return render(request, 'profesor_principal/modificar_profesor.html', {'profesor': profesor})

        try:
            # Update professor with new data
            for key, value in form_data.items():
                setattr(profesor, key, value)
            profesor.save()
            messages.success(request, "Profesor actualizado correctamente.")
            return redirect('p_profesores')
        except Exception as e:
            messages.error(request, f"Error al actualizar el profesor: {str(e)}")
            return render(request, 'profesor_principal/modificar_profesor.html', {'profesor': profesor})

    return render(request, 'profesor_principal/modificar_profesor.html', {'profesor': profesor})

def visualizarProfesor(request, profesor_id):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    """View a single strategy."""
    profesor = get_object_or_404(Profesor, id=profesor_id)
    return render(request, 'profesor_principal/visualizar_profesor.html', {'profesor': profesor})