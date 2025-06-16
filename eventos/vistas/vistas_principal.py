from django.shortcuts import render, get_object_or_404, redirect
from eventos.models import Evento
from profesores.models import Profesor
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator

def visualizar_eventos(request):
    """Display all events with optional search functionality and pagination."""
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
    
    paginator = Paginator(eventos, 4)  # 4 eventos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'profesor_principal/listar_eventos.html', {
        'eventos': page_obj.object_list,
        'page_obj': page_obj,
        'query': query
    })

def crear_evento(request):
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
            messages.success(request, "Registro satisfactorio.")
            return redirect('p_eventos')
        except Exception as e:
            print(str(e))
            messages.error(request, f"Error al registrar el evento: {str(e)}")

    profesores = Profesor.objects.all()
    return render(request, 'profesor_principal/formular_evento.html', {'profesores': profesores})

def eliminar_evento(request, evento_id):
    """Delete a single event."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    messages.success(request, "Eliminación satisfactoria.")
    return redirect('p_eventos')

def eliminar_eventos(request):
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
            messages.success(request, "Eliminación satisfactoria.")
        else:
            messages.error(request, "No se seleccionaron eventos para eliminar.")
        return redirect('p_eventos')
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def modificar_evento(request, evento_id):
    """Modify a single event."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    
    profesores = Profesor.objects.all()
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        profesor_id = request.POST.get('profesor_encargado')
        try:
            profesor_obj = Profesor.objects.get(id=int(profesor_id))  # << Fix aquí
        except (Profesor.DoesNotExist, ValueError, TypeError):
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

        if not all(form_data.values()):
            messages.error(request, "Todos los campos obligatorios deben ser completados.")
            return render(request, 'profesor_principal/modificar_evento.html', {'evento': evento, 'profesores': profesores})

        try:
            for key, value in form_data.items():
                setattr(evento, key, value)
            evento.save()
            messages.success(request, "Actualización satisfactoria.")
            return redirect('p_eventos')
        except Exception as e:
            messages.error(request, f"Error al actualizar el evento: {str(e)}")
            return render(request, 'profesor_principal/modificar_evento.html', {'evento': evento, 'profesores': profesores})

    return render(request, 'profesor_principal/modificar_evento.html', {'evento': evento, 'profesores': profesores})

def visualizar_evento(request, evento_id):
    """View a single event."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'profesor_principal/visualizar_evento.html', {'evento': evento})