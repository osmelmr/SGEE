from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Evento, Profesor
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

def visualizarEventos(request):
    """Display all events with optional search functionality."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    query = request.GET.get('q', '')
    if query:
        eventos = Evento.objects.filter(
            Q(nombre_evento__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(ubicacion_evento__icontains=query) |
            Q(tipo_evento__icontains=query) |
            Q(telefono_contacto__icontains=query) |
            Q(profesor_encargado__nombre__icontains=query) |
            Q(profesor_encargado__primer_apellido__icontains=query)
        )
    else:
        eventos = Evento.objects.all()
    return render(request, 'profesor_principal/listar_eventos.html', {
        'eventos': eventos,
        'query': query
    })

def crearEvento(request):
    """Handle event form submission and display."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    if request.method == 'POST':
        profesor_id = request.POST.get('profesor_encargado')
        try:
            profesor_obj = Profesor.objects.get(id=profesor_id)
        except Profesor.DoesNotExist:
            profesor_obj = None

        form_data = {
            'nombre_evento': request.POST.get('nombre_evento'),
            'fecha_inicio': request.POST.get('fecha_inicio'),
            'fecha_fin': request.POST.get('fecha_fin'),
            'hora_inicio': request.POST.get('hora_inicio'),
            'hora_fin': request.POST.get('hora_fin'),
            'ubicacion_evento': request.POST.get('ubicacion_evento'),
            'tipo_evento': request.POST.get('tipo_evento'),
            'descripcion': request.POST.get('descripcion'),
            'profesor_encargado': profesor_obj,
            'telefono_contacto': request.POST.get('telefono_contacto')
        }
        
        # Validate required fields
        if not all(form_data.values()):
            messages.error(request, "Todos los campos obligatorios deben ser completados.")
            return render(request, 'profesor_principal/formular_evento.html')

        try:
            evento = Evento(**form_data)
            evento.save()
            messages.success(request, "Evento registrado correctamente.")
            return redirect('eventos')
        except Exception as e:
            print(str(e))
            messages.error(request, f"Error al registrar el evento: {str(e)}")

    profesores = Profesor.objects.all()
    return render(request, 'profesor_principal/formular_evento.html', {'profesores': profesores})

def eliminarEvento(request, evento_id):
    """Delete a single event."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    messages.success(request, "Evento eliminado correctamente.")
    return redirect('eventos')

def eliminarEventos(request):
    """Delete multiple events."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    if request.method == 'POST':
        eventos_ids = request.POST.getlist('eventos[]')
        if eventos_ids:
            Evento.objects.filter(id__in=eventos_ids).delete()
            messages.success(request, "Eventos eliminados correctamente.")
        else:
            messages.error(request, "No se seleccionaron eventos para eliminar.")
        return redirect('eventos')
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def modificarEvento(request, evento_id):
    """Modify a single event."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    evento = get_object_or_404(Evento, id=evento_id)
    
    if request.method == 'POST':
        profesor_id = request.POST.get('profesor_encargado')
        try:
            profesor_obj = Profesor.objects.get(id=profesor_id)
        except Profesor.DoesNotExist:
            profesor_obj = None

        form_data = {
            'nombre_evento': request.POST.get('nombre_evento'),
            'fecha_inicio': request.POST.get('fecha_inicio'),
            'fecha_fin': request.POST.get('fecha_fin'),
            'hora_inicio': request.POST.get('hora_inicio'),
            'hora_fin': request.POST.get('hora_fin'),
            'ubicacion_evento': request.POST.get('ubicacion_evento'),
            'tipo_evento': request.POST.get('tipo_evento'),
            'descripcion': request.POST.get('descripcion'),
            'profesor_encargado': profesor_obj,
            'telefono_contacto': request.POST.get('telefono_contacto')
        }
        
        # Validate required fields
        if not all(form_data.values()):
            messages.error(request, "Todos los campos obligatorios deben ser completados.")
            return render(request, 'profesor_principal/modificar_evento.html', {'evento': evento})

        try:
            # Update event with new data
            for key, value in form_data.items():
                setattr(evento, key, value)
            evento.save()
            messages.success(request, "Evento actualizado correctamente.")
            return redirect('eventos')
        except Exception as e:
            messages.error(request, f"Error al actualizar el evento: {str(e)}")
            return render(request, 'profesor_principal/modificar_evento.html', {'evento': evento})

    return render(request, 'profesor_principal/modificar_evento.html', {'evento': evento})

def visualizarEvento(request, evento_id):
    """View a single event."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'profesor_principal/visualizar_evento.html', {'evento': evento})