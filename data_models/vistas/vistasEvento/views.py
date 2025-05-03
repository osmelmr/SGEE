from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Evento
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

def visualizarEventos(request):
    """Display all strategies with optional search functionality."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            query = request.GET.get('q', '')
            if query:
                # Search in multiple fields
                eventos = Evento.objects.filter(
                    Q(nombre__icontains=query) |
                    Q(curso__icontains=query) |
                    Q(anio_escolar__icontains=query) |
                    Q(grupo__icontains=query) |
                    Q(autor__icontains=query)
                )
            else:
                eventos = Evento.objects.all()
            
            return render(request, 'profesor_principal/listar_eventos.html', {
                'eventos': eventos,
                'query': query
            })
        else:
            messages.error(request, "No tienes permiso para visualizar eventos.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

# Form Views
# ----------------------------------------------------------------------------
def crearEvento(request):
    """Handle event form submission and display."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            if request.method == 'POST':
                # Extract form data
                form_data = {
                    'nombre_evento': request.POST.get('nombre-evento'),
                    'fecha_inicio': request.POST.get('fecha-inicio'),
                    'fecha_fin': request.POST.get('fecha-fin'),
                    'hora_inicio': request.POST.get('hora-inicio'),
                    'hora_fin': request.POST.get('hora-fin'),
                    'ubicacion_evento': request.POST.get('ubicacion-evento'),
                    'tipo_evento': request.POST.get('tipo-evento'),
                    'descripcion': request.POST.get('descripcion-evento'),
                    'profesor_encargado': request.POST.get('profesor-cargo'),
                    'telefono_contacto': request.POST.get('telefono-contacto')
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
                    messages.error(request, f"Error al registrar el evento: {str(e)}")

            return render(request, 'profesor_principal/formular_evento.html')
        else:
            messages.error(request, "No tienes permiso para crear eventos.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

# Delete Views - Single Item
# ----------------------------------------------------------------------------
def eliminarEvento(request, evento_id):
    """Delete a single event."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            evento = get_object_or_404(Evento, id=evento_id)
            evento.delete()
            messages.success(request, "Evento eliminado correctamente.")
            return redirect('eventos')
        else:
            messages.error(request, "No tienes permiso para eliminar eventos.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

# Delete Views - Multiple Items
# ----------------------------------------------------------------------------
def eliminarEventos(request):
    """Delete multiple events."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            if request.method == 'POST':
                eventos_ids = request.POST.getlist('eventos[]')
                if eventos_ids:
                    Evento.objects.filter(id__in=eventos_ids).delete()
                    messages.success(request, "Eventos eliminados correctamente.")
                else:
                    messages.error(request, "No se seleccionaron eventos para eliminar.")
                return redirect('eventos')
            return JsonResponse({'error': 'Método no permitido'}, status=405)
        else:
            messages.error(request, "No tienes permiso para eliminar eventos.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def modificarEvento(request, evento_id):
    """Modify a single event."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            evento = get_object_or_404(Evento, id=evento_id)
            
            if request.method == 'POST':
                # Extract form data
                form_data = {
                    'nombre_evento': request.POST.get('nombre-evento'),
                    'fecha_inicio': request.POST.get('fecha-inicio'),
                    'fecha_fin': request.POST.get('fecha-fin'),
                    'hora_inicio': request.POST.get('hora-inicio'),
                    'hora_fin': request.POST.get('hora-fin'),
                    'ubicacion_evento': request.POST.get('ubicacion-evento'),
                    'tipo_evento': request.POST.get('tipo-evento'),
                    'descripcion': request.POST.get('descripcion-evento'),
                    'profesor_encargado': request.POST.get('profesor-cargo'),
                    'telefono_contacto': request.POST.get('telefono-contacto')
                }
                
                # Validate required fields
                if not all(form_data.values()):
                    messages.error(request, "Todos los campos obligatorios deben ser completados.")
                    return render(request, 'modificar_evento.html', {'evento': evento})

                try:
                    # Update event with new data
                    for key, value in form_data.items():
                        setattr(evento, key, value)
                    evento.save()
                    messages.success(request, "Evento actualizado correctamente.")
                    return redirect('eventos')
                except Exception as e:
                    messages.error(request, f"Error al actualizar el evento: {str(e)}")
                    return render(request, 'modificar_evento.html', {'evento': evento})

            return render(request, 'modificar_evento.html', {'evento': evento})
        else:
            messages.error(request, "No tienes permiso para modificar eventos.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def visualizarEvento(request, evento_id):
    """View a single event."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            evento = get_object_or_404(Evento, id=evento_id)
            return render(request, 'profesor_principal/visualizar_evento.html', {'evento': evento})
        else:
            messages.error(request, "No tienes permiso para visualizar eventos.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")