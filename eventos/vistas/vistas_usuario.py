from django.shortcuts import render, get_object_or_404, redirect
from eventos.models import Evento
from django.contrib import messages
from django.db.models import Q



def visualizar_eventos(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar todos los eventos."""
    query = request.GET.get("q", "")
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
    
    # Obtener los IDs de los eventos a los que el usuario está inscrito
    if hasattr(request.user, 'eventos'):
        eventos_inscritos_ids = list(request.user.eventos.values_list('id', flat=True))
    else:
        eventos_inscritos_ids = []

    return render(
        request,
        "usuarios/listar_eventos.html",
        {
            "eventos": eventos,
            "query": query,
            "eventos_inscritos_ids": eventos_inscritos_ids
        }
    )

def visualizar_evento(request, evento_id):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar un evento específico."""
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, "usuarios/visualizar_evento.html", {"evento": evento})

def toggleEvento(request, evento_id):
    if request.user.is_authenticated:
        try:
            # Obtener el evento por su ID
            evento = get_object_or_404(Evento, id=evento_id)
            
            # Obtener el usuario actual
            usuario = request.user
            
            # Verificar si el evento ya está asociado al usuario
            if evento in usuario.eventos.all():
                # Si el evento ya está asociado, eliminarlo
                usuario.eventos.remove(evento)
                messages.success(request, f"Te has desregistrado del evento '{evento.nombre_evento}' correctamente.")
            else:
                # Si el evento no está asociado, agregarlo
                usuario.eventos.add(evento)
                messages.success(request, f"Te has registrado en el evento '{evento.nombre_evento}' correctamente.")
        except Exception as e:
            messages.error(request, f"Error al procesar el evento: {str(e)}")
    else:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
    return redirect('eventos')
