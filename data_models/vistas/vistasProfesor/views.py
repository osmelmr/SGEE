from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Profesor
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

def visualizarProfesores(request):
    if request.user.is_authenticated:
        if request.user.es_profesor():
            """Display all strategies with optional search functionality."""
            query = request.GET.get('q', '')
            if query:
                # Search in multiple fields
                profesores = Profesor.objects.filter(
                    Q(nombre__icontains=query) |
                    Q(curso__icontains=query) |
                    Q(anio_escolar__icontains=query) |
                    Q(grupo__icontains=query) |
                    Q(autor__icontains=query)
                )
            else:
                profesores = Profesor.objects.all()
            
            return render(request, 'profesor_principal/listar_profesores.html', {
                'profesores': profesores,
                'query': query
            })
        else:
            messages.error(request, "No tienes permiso para visualizar profesores.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

def crearProfesor(request):
    if request.user.is_authenticated:
        if request.user.es_profesor():
            """Handle professor information form submission and display."""
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
                    return render(request, 'profesor_principal/formular_profesor.html')

                try:
                    profesor = Profesor.objects.create(**form_data)
                    messages.success(request, "Profesor registrado correctamente.")
                    return redirect('profesores')
                except Exception as e:
                    messages.error(request, f"Error al registrar el profesor: {str(e)}")

            return render(request, 'profesor_principal/formular_profesor.html')
        else:
            messages.error(request, "No tienes permiso para crear profesores.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

def eliminarProfesor(request, profesor_id):
    if request.user.is_authenticated:
        if request.user.es_profesor():
            """Delete a single professor."""
            profesor = get_object_or_404(Profesor, id=profesor_id)
            profesor.delete()
            messages.success(request, "Profesor eliminado correctamente.")
            return redirect('profesores')
        else:
            messages.error(request, "No tienes permiso para eliminar profesores.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

def eliminarProfesores(request):
    if request.user.is_authenticated:
        if request.user.es_profesor():
            """Delete multiple strategies."""
            if request.method == 'POST':
                profesores_ids = request.POST.getlist('profesores[]')
                if profesores_ids:
                    Profesor.objects.filter(id__in=profesores_ids).delete()
                    messages.success(request, "Profesores eliminadas correctamente.")
                else:
                    messages.error(request, "No se seleccionaron profesores para eliminar.")
                return redirect('profesores')
            return JsonResponse({'error': 'Método no permitido'}, status=405)
        else:
            messages.error(request, "No tienes permiso para eliminar profesores.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

def modificarProfesor(request, profesor_id):
    if request.user.is_authenticated:
        if request.user.es_profesor():
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
                    return redirect('profesores')
                except Exception as e:
                    messages.error(request, f"Error al actualizar el profesor: {str(e)}")
                    return render(request, 'profesor_principal/modificar_profesor.html', {'profesor': profesor})

            return render(request, 'profesor_principal/modificar_profesor.html', {'profesor': profesor})
        else:
            messages.error(request, "No tienes permiso para modificar profesores.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

def visualizarProfesor(request, profesor_id):
    if request.user.is_authenticated:
        if request.user.es_profesor():
            """View a single strategy."""
            profesor = get_object_or_404(Profesor, id=profesor_id)
            return render(request, 'profesor_principal/visualizar_profesor.html', {'profesor': profesor})
        else:
            messages.error(request, "No tienes permiso para visualizar profesores.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")