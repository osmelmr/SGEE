from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Profesor
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

def visualizarProfesores(request):
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
    
    return render(request, 'profesores.html', {
        'profesores': profesores,
        'query': query
    })

# Form Views
# ----------------------------------------------------------------------------
def crearProfesor(request):
    """Handle professor information form submission and display."""
    if request.method == 'POST':
        
        form_data = {
            'nombre': request.POST.get('nombre-profesor'),
            'primer_apellido': request.POST.get('primer-apellido'),
            'segundo_apellido': request.POST.get('segundo-apellido'),
            'sexo': request.POST.get('sexo'),
            'categoria_docente': request.POST.get('categoria-docente'),
            'asignatura': request.POST.get('asignatura'),
            'solapin': request.POST.get('solapin'),
            'telefono': request.POST.get('telefono'),
            'correo': request.POST.get('correo'),
            'brigada_asignada': request.POST.get('brigada-asignada'),
            'descripcion': request.POST.get('descripcion-profesor')
        }
        # Validate required fields
        if not all(form_data.values()):
            messages.error(request, "Todos los campos obligatorios deben ser completados.")
            return render(request, 'formulario_informacion_pro.html')

        try:
            profesor = Profesor(**form_data)
            print(profesor)
            profesor.save()
            messages.success(request, "Profesor registrado correctamente.")
            return redirect('profesores')
        except Exception as e:
            messages.error(request, f"Error al registrar el profesor: {str(e)}")

    return render(request, 'formulario_informacion_pro.html')

# Delete Views - Single Item
# ----------------------------------------------------------------------------
def eliminarProfesor(request, profesor_id):
    """Delete a single professor."""
    profesor = get_object_or_404(Profesor, id=profesor_id)
    profesor.delete()
    messages.success(request, "Profesor eliminado correctamente.")
    return redirect('profesores')

# Delete Views - Multiple Items
# ----------------------------------------------------------------------------
def eliminarProfesores(request):
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

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def modificarProfesor(request, profesor_id):
    """Modify a single professor."""
    profesor = get_object_or_404(Profesor, id=profesor_id)
    
    if request.method == 'POST':
        # Eliminar 'brigadas_impartir' del diccionario form_data
        form_data = {
            'nombre': request.POST.get('nombre'),
            'primer_apellido': request.POST.get('primer-apellido'),
            'segundo_apellido': request.POST.get('segundo-apellido'),
            'sexo': request.POST.get('sexo'),
            'categoria_docente': request.POST.get('categoria-docente'),
            'asignatura': request.POST.get('asignatura'),
            'solapin': request.POST.get('solapin'),
            'telefono': request.POST.get('telefono'),
            'correo': request.POST.get('correo'),
            'brigada_asignada': request.POST.get('brigada-asignada'),
            'descripcion': request.POST.get('descripcion')
        }

        # Validate required fields
        if not all(form_data.values()):
            messages.error(request, "Todos los campos obligatorios deben ser completados.")
            return render(request, 'modificar_profesor.html', {'profesor': profesor})

        try:
            # Update professor with new data
            for key, value in form_data.items():
                setattr(profesor, key, value)
            profesor.save()
            messages.success(request, "Profesor actualizado correctamente.")
            return redirect('profesores')
        except Exception as e:
            messages.error(request, f"Error al actualizar el profesor: {str(e)}")
            return render(request, 'modificar_profesor.html', {'profesor': profesor})

    return render(request, 'modificar_profesor.html', {'profesor': profesor})

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def visualizarProfesor(request, profesor_id):
    """View a single strategy."""
    profesor = get_object_or_404(Profesor, id=profesor_id)
    return render(request, 'visualizar_profesor.html', {'profesor': profesor})