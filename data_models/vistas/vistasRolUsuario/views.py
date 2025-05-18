from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Reporte, Grupo, Estrategia, Evento, Profesor, Encuesta, Usuario
from django.contrib import messages
from data_models.models import Respuesta, Pregunta
from django.http import HttpResponse

def visualizarEstrategiasG(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar todas las estrategias."""
    estrategias = Estrategia.objects.all()
    return render(request, "usuarios/listar_estrategias.html", {"estrategias": estrategias})

def principalG(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Página principal con la lista de grupos."""
    grupos = Grupo.objects.all()
    return render(request, "usuarios/pagina_principal.html", {"grupos": grupos})

def visualizarEstrategiaG(request, estrategia_id):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar una estrategia específica."""
    estrategia = get_object_or_404(Estrategia, id=estrategia_id)
    return render(request, "usuarios/visualizar_estrategia.html", {"estrategia": estrategia})

def visualizarProfesoresG(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar todos los profesores."""
    profesores = Profesor.objects.all()
    return render(request, "usuarios/listar_profesores.html", {"profesores": profesores})

def visualizarProfesorG(request, profesor_id):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar un profesor específico."""
    profesor = get_object_or_404(Profesor, id=profesor_id)
    return render(request, "usuarios/visualizar_profesor.html", {"profesor": profesor})

def visualizarEventosG(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar todos los eventos."""
    eventos = Evento.objects.all()
    return render(request, "usuarios/listar_eventos.html", {"eventos": eventos})

def visualizarEventoG(request, evento_id):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar un evento específico."""
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, "usuarios/visualizar_evento.html", {"evento": evento})

def visualizarReportesG(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar todos los reportes."""
    reportes = Reporte.objects.all()
    return render(request, "usuarios/listar_reportes.html", {"reportes": reportes})

def visualizarReporteG(request, reporte_id):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar un reporte específico."""
    reporte = get_object_or_404(Reporte, id=reporte_id)
    return render(request, "usuarios/visualizar_reporte.html", {"reporte": reporte})

def visualizarEncuestasG(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar solo las encuestas que el usuario no ha realizado."""
    usuario = request.user
    # Suponiendo que Usuario tiene un ManyToManyField a Encuesta llamado 'encuestas_realizadas'
    encuestas_realizadas = usuario.encuestas_realizadas.all()
    encuestas = Encuesta.objects.exclude(id__in=encuestas_realizadas.values_list('id', flat=True))
    return render(request, "usuarios/listar_encuestas.html", {"encuestas": encuestas})

def visualizarEncuestaG(request, encuesta_id):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar una encuesta específica."""
    encuesta = get_object_or_404(Encuesta, id=encuesta_id)
    return render(request, "usuarios/visualizar_encuesta.html", {"encuesta": encuesta})

def contact_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Render the contact page."""
    return render(request, 'usuarios/contactenos.html')

def sobrenos_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Render the about us page."""
    return render(request, 'usuarios/sobrenos.html')

def visualizarTestimonios(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Render the testimonials page."""
    return render(request, 'usuarios/testimonials.html')

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
    return redirect('eventos_g')

def realizar_encuesta(request, encuesta_id):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

    encuesta = get_object_or_404(Encuesta, id=encuesta_id)
    preguntas = encuesta.preguntas.all()

    if request.method == 'POST':
        # Recoger respuestas del formulario
        respuestas = []
        for key in request.POST:
            if key.startswith('pregunta_'):
                pregunta_id = key.split('_')[1]
                valor = request.POST[key]
                pregunta = get_object_or_404(Pregunta, id=pregunta_id)
                respuestas.append(Respuesta(
                    pregunta=pregunta,
                    encuesta=encuesta,
                    evaluacion=valor
                ))
        # Guardar todas las respuestas
        Respuesta.objects.bulk_create(respuestas)

        # Agregar la encuesta a la lista de encuestas realizadas del usuario
        request.user.encuestas_realizadas.add(encuesta)

        messages.success(request, "¡Respuestas enviadas correctamente!")
        return redirect('pagina_principal_g')

    return render(request, 'usuarios/realizar_encuesta.html', {
        'encuesta': encuesta,
        'preguntas': preguntas,
    })