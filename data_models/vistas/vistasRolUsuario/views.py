from django.shortcuts import render, get_object_or_404
from data_models.models import Reporte, Grupo, Estrategia, Evento, Profesor, Encuesta

def visualizarEstrategiasG(request):
    """Visualizar todas las estrategias."""
    estrategias = Estrategia.objects.all()
    return render(request, "usuarios/listar_estrategias.html", {"estrategias": estrategias})

def principalG(request):
    """Página principal con la lista de grupos."""
    grupos = Grupo.objects.all()
    return render(request, "usuarios/pagina_principal.html", {"grupos": grupos})

def visualizarEstrategiaG(request, estrategia_id):
    """Visualizar una estrategia específica."""
    estrategia = get_object_or_404(Estrategia, id=estrategia_id)
    return render(request, "usuarios/visualizar_estrategia.html", {"estrategia": estrategia})

def visualizarProfesoresG(request):
    """Visualizar todos los profesores."""
    profesores = Profesor.objects.all()
    return render(request, "usuarios/listar_profesores.html", {"profesores": profesores})

def visualizarProfesorG(request, profesor_id):
    """Visualizar un profesor específico."""
    profesor = get_object_or_404(Profesor, id=profesor_id)
    return render(request, "usuarios/visualizar_profesor.html", {"profesor": profesor})

def visualizarEventosG(request):
    """Visualizar todos los eventos."""
    eventos = Evento.objects.all()
    return render(request, "usuarios/listar_eventos.html", {"eventos": eventos})

def visualizarEventoG(request, evento_id):
    """Visualizar un evento específico."""
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, "usuarios/visualizar_evento.html", {"evento": evento})

def visualizarReportesG(request):
    """Visualizar todos los reportes."""
    reportes = Reporte.objects.all()
    return render(request, "usuarios/listar_reportes.html", {"reportes": reportes})

def visualizarReporteG(request, reporte_id):
    """Visualizar un reporte específico."""
    reporte = get_object_or_404(Reporte, id=reporte_id)
    return render(request, "usuarios/visualizar_reporte.html", {"reporte": reporte})

def visualizarEncuestasG(request):
    """Visualizar todas las encuestas."""
    encuestas = Encuesta.objects.all()
    return render(request, "usuarios/listar_encuestas.html", {"encuestas": encuestas})

def visualizarEncuestaG(request, encuesta_id):
    """Visualizar una encuesta específica."""
    encuesta = get_object_or_404(Encuesta, id=encuesta_id)
    return render(request, "usuarios/visualizar_encuesta.html", {"encuesta": encuesta})

def contact_view(request):
    """Render the contact page."""
    return render(request, 'usuarios/contactenos.html')

def sobrenos_view(request):
    """Render the about us page."""
    return render(request, 'usuarios/sobrenos.html')

def visualizarTestimonios(request):
    """Render the testimonials page."""
    return render(request, 'usuarios/testimonials.html')