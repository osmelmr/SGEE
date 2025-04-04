"""
Views for the SGEE (Sistema de Gestión de Estrategias Educativas) application.
This module contains all the views for handling different aspects of the educational management system.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from data_models.models import Estrategia, Evento, Profesor, Reporte, Encuesta
from django.http import JsonResponse

# Static Pages
# ----------------------------------------------------------------------------
def estra_view(request):
    """Render the main strategy page."""
    return render(request, 'estra.html')

def contact_view(request):
    """Render the contact page."""
    return render(request, 'contactenos.html')

def sobrenos_view(request):
    """Render the about us page."""
    return render(request, 'sobrenos.html')

def visualizarTestimonios(request):
    """Render the testimonials page."""
    return render(request, 'testimonials.html')

# # List Views
# # ----------------------------------------------------------------------------
# def estrategias_view(request):
#     """Display all strategies."""
#     estrat = Estrategia.objects.all()
#     return render(request, 'estrategias.html', {'estrategias': estrat})

# def eventos_view(request):
#     """Display all events."""
#     eventos = Evento.objects.all()
#     return render(request, 'eventos.html', {'eventos': eventos})

# def reportes_view(request):
#     """Display all reports."""
#     reportes = Reporte.objects.all()
#     return render(request, 'reportes.html', {'reportes': reportes})

# def usuarios_view(request):
#     """Display all users."""
#     return render(request, 'usuarios.html')

# def informacion_profesoral_view(request):
#     """Display all professors information."""
#     profesores = Profesor.objects.all()
#     return render(request, 'profesores.html', {'profesores': profesores})

# def encuestas_view(request):
#     """Display all surveys."""
#     encuestas = Encuesta.objects.all()
#     return render(request, 'encuestas.html', {'encuestas': encuestas})

# # Form Views
# # ----------------------------------------------------------------------------
# def formulario_estrategia_view(request):
#     """Handle strategy form submission and display."""
#     if request.method == 'POST':
#         # Extract form data
#         form_data = {
#             'nombre': request.POST.get('titulo-estrategia'),
#             'curso': request.POST.get('curso'),
#             'anio_escolar': request.POST.get('ano-escolar'),
#             'grupo': request.POST.get('grupo'),
#             'plan_estudios': request.POST.get('plan-estudios'),
#             'obj_estrategia': request.POST.get('objetivos-estrategia'),
#             'dir_brigada': request.POST.get('direccion-brigada'),
#             'caract_brigada': request.POST.get('caracteristicas-brigada'),
#             'colect_pedagogico': request.POST.get('colectivo-pedagogico'),
#             'otros_aspectos': request.POST.get('otros-aspectos', 'otros_aspectos'),
#             'dim_curricular': request.POST.get('dimension-curricular'),
#             'dim_extensionista': request.POST.get('dimension-extensionista'),
#             'dim_politica': request.POST.get('dimension-politico-ideologica'),
#             'conclusiones': request.POST.get('conclusiones'),
#             'obj_general': request.POST.get('objetivo-general'),
#             'obj_dc': request.POST.get('objetivos-especificos-curricular'),
#             'plan_dc': request.POST.get('plan-acciones-curricular'),
#             'obj_de': request.POST.get('objetivos-especificos-extensionista'),
#             'plan_de': request.POST.get('plan-acciones-extensionista'),
#             'obj_dp': request.POST.get('objetivos-especificos-politico-ideologica'),
#             'plan_dp': request.POST.get('plan-acciones-politico-ideologica'),
#             'evaluacion': request.POST.get('evaluacion-integral'),
#             'autor': request.POST.get('autor'),
#         }
        
#         try:
#             estrategia = Estrategia(**form_data)
#             estrategia.save()
#             messages.success(request, "Estrategia registrada correctamente.")
#             return redirect('estrategias')
#         except Exception as e:
#             messages.error(request, f"Error al registrar la estrategia: {str(e)}")
    
#     return render(request, 'formulario_estrategia.html')

# def formulario_evento_view(request):
#     """Handle event form submission and display."""
#     if request.method == 'POST':
#         # Extract form data
#         form_data = {
#             'nombre_evento': request.POST.get('nombre-evento'),
#             'fecha_inicio': request.POST.get('fecha-inicio'),
#             'fecha_fin': request.POST.get('fecha-fin'),
#             'hora_inicio': request.POST.get('hora-inicio'),
#             'hora_fin': request.POST.get('hora-fin'),
#             'ubicacion_evento': request.POST.get('ubicacion-evento'),
#             'tipo_evento': request.POST.get('tipo-evento'),
#             'descripcion': request.POST.get('descripcion-evento'),
#             'profesor_cargo': request.POST.get('profesor-cargo'),
#             'telefono_contacto': request.POST.get('telefono-contacto')
#         }

#         # Validate required fields
#         if not all(form_data.values()):
#             messages.error(request, "Todos los campos obligatorios deben ser completados.")
#             return render(request, 'formulario_evento.html')

#         try:
#             evento = Evento(**form_data)
#             evento.save()
#             messages.success(request, "Evento registrado correctamente.")
#             return redirect('eventos')
#         except Exception as e:
#             messages.error(request, f"Error al registrar el evento: {str(e)}")

#     return render(request, 'formulario_evento.html')

# def formulario_reporte_view(request):
#     """Handle report form submission and display."""
#     if request.method == 'POST':
#         # Extract form data
#         form_data = {
#             'brigada': request.POST.get('brigada'),
#             'codigo': request.POST.get('codigo'),
#             'periodo': request.POST.get('periodo'),
#             'fecha': request.POST.get('fecha'),
#             'autor': request.POST.get('autor'),
#             'institucion': request.POST.get('institucion'),
#             'resumen': request.POST.get('resumen'),
#             'objetivos': request.POST.get('objetivos'),
#             'actividades': request.POST.get('actividades'),
#             'resultados': request.POST.get('resultados'),
#             'analisis': request.POST.get('analisis'),
#             'desafios': request.POST.get('desafios'),
#             'proximos_pasos': request.POST.get('proximos-pasos'),
#             'anexos': request.FILES.get('anexos')
#         }

#         try:
#             reporte = Reporte(**form_data)
#             reporte.save()
#             messages.success(request, "Reporte registrado correctamente.")
#             return redirect('reportes')
#         except Exception as e:
#             messages.error(request, f"Error al registrar el reporte: {str(e)}")

#     return render(request, 'formulario_reporte.html')

# def formulario_informacion_pro_view(request):
#     """Handle professor information form submission and display."""
#     if request.method == 'POST':
#         # Extract form data
#         form_data = {
#             'nombre': request.POST.get('nombre-profesor'),
#             'primer_apellido': request.POST.get('primer-apellido'),
#             'segundo_apellido': request.POST.get('segundo-apellido'),
#             'sexo': request.POST.get('sexo'),
#             'categoria_docente': request.POST.get('categoria-docente'),
#             'asignatura': request.POST.get('asignatura'),
#             'solapin': request.POST.get('solapin'),
#             'telefono': request.POST.get('telefono'),
#             'correo': request.POST.get('correo'),
#             'brigada_asignada': request.POST.get('brigada-asignada'),
#             'brigadas_impartir': request.POST.get('brigadas-impartir'),
#             'descripcion': request.POST.get('descripcion-profesor')
#         }

#         # Validate required fields
#         if not all(form_data.values()):
#             messages.error(request, "Todos los campos obligatorios deben ser completados.")
#             return render(request, 'formulario_informacion_pro.html')

#         try:
#             profesor = Profesor(**form_data)
#             profesor.save()
#             messages.success(request, "Profesor registrado correctamente.")
#             return redirect('profesores')
#         except Exception as e:
#             messages.error(request, f"Error al registrar el profesor: {str(e)}")

#     return render(request, 'formulario_informacion_pro.html')

# def formulario_encuesta_view(request):
#     """Handle survey form submission and display."""
#     return render(request, 'formulario_encuesta.html')

# def formulario_usuario_view(request):
#     """Handle user form submission and display."""
#     return render(request, 'formulario_usuario.html')

# # Delete Views - Single Item
# # ----------------------------------------------------------------------------
# def eliminarEstrategia(request, estra_id):
#     """Delete a single strategy."""
#     estra = get_object_or_404(Estrategia, id=estra_id)
#     estra.delete()
#     messages.success(request, "Estrategia eliminada correctamente.")
#     return redirect('estrategias')

# def eliminar_evento(request, evento_id):
#     """Delete a single event."""
#     evento = get_object_or_404(Evento, id=evento_id)
#     evento.delete()
#     messages.success(request, "Evento eliminado correctamente.")
#     return redirect('eventos')

# def eliminar_reporte(request, reporte_id):
#     """Delete a single report."""
#     reporte = get_object_or_404(Reporte, id=reporte_id)
#     reporte.delete()
#     messages.success(request, "Reporte eliminado correctamente.")
#     return redirect('reportes')

# def eliminar_profesor(request, profesor_id):
#     """Delete a single professor."""
#     profesor = get_object_or_404(Profesor, id=profesor_id)
#     profesor.delete()
#     messages.success(request, "Profesor eliminado correctamente.")
#     return redirect('profesores')

# def eliminar_encuesta(request, encuesta_id):
#     """Delete a single survey."""
#     encuesta = get_object_or_404(Encuesta, id=encuesta_id)
#     encuesta.delete()
#     messages.success(request, "Encuesta eliminada correctamente.")
#     return redirect('encuestas')

# # Delete Views - Multiple Items
# # ----------------------------------------------------------------------------
# def eliminar_estrategias(request):
#     """Delete multiple strategies."""
#     if request.method == 'POST':
#         estrategias_ids = request.POST.getlist('estrategias[]')
#         if estrategias_ids:
#             Estrategia.objects.filter(id__in=estrategias_ids).delete()
#             messages.success(request, "Estrategias eliminadas correctamente.")
#         else:
#             messages.error(request, "No se seleccionaron estrategias para eliminar.")
#         return redirect('estrategias')
#     return JsonResponse({'error': 'Método no permitido'}, status=405)

# def eliminar_eventos(request):
#     """Delete multiple events."""
#     if request.method == 'POST':
#         eventos_ids = request.POST.getlist('eventos[]')
#         if eventos_ids:
#             Evento.objects.filter(id__in=eventos_ids).delete()
#             messages.success(request, "Eventos eliminados correctamente.")
#         else:
#             messages.error(request, "No se seleccionaron eventos para eliminar.")
#         return redirect('eventos')
#     return JsonResponse({'error': 'Método no permitido'}, status=405)

# def eliminarProfesores(request):
#     """Delete multiple professors."""
#     if request.method == 'POST':
#         profesores_ids = request.POST.getlist('profesores[]')
#         if profesores_ids:
#             Profesor.objects.filter(id__in=profesores_ids).delete()
#             messages.success(request, "Profesores eliminados correctamente.")
#         else:
#             messages.error(request, "No se seleccionaron profesores para eliminar.")
#         return redirect('profesores')
#     return JsonResponse({'error': 'Método no permitido'}, status=405)

# def eliminar_encuestas(request):
#     """Delete multiple surveys."""
#     if request.method == 'POST':
#         encuestas_ids = request.POST.getlist('encuestas[]')
#         if encuestas_ids:
#             Encuesta.objects.filter(id__in=encuestas_ids).delete()
#             messages.success(request, "Encuestas eliminadas correctamente.")
#         else:
#             messages.error(request, "No se seleccionaron encuestas para eliminar.")
#         return redirect('encuestas')
#     return JsonResponse({'error': 'Método no permitido'}, status=405)

# def eliminar_reportes(request):
#     """Delete multiple reports."""
#     if request.method == 'POST':
#         reportes_ids = request.POST.getlist('reportes[]')
#         if reportes_ids:
#             Reporte.objects.filter(id__in=reportes_ids).delete()
#             messages.success(request, "Reportes eliminados correctamente.")
#         else:
#             messages.error(request, "No se seleccionaron reportes para eliminar.")
#         return redirect('reportes')
#     return JsonResponse({'error': 'Método no permitido'}, status=405)

# def eliminar_usuarios(request):
#     """Delete multiple users."""
#     if request.method == 'POST':
#         usuarios_ids = request.POST.getlist('usuarios[]')
#         if usuarios_ids:
#             Usuario.objects.filter(id__in=usuarios_ids).delete()
#             messages.success(request, "Usuarios eliminados correctamente.")
#         else:
#             messages.error(request, "No se seleccionaron usuarios para eliminar.")
#         return redirect('usuarios')
#     return JsonResponse({'error': 'Método no permitido'}, status=405)

# # Update Views - Unique Item
# # ----------------------------------------------------------------------------
# def modificarEstrategia(request, estra_id):
#     """Modify a single strategy."""
#     estra = get_object_or_404(Estrategia, id=estra_id)
#     return render(request, 'modificar_estrategia.html', {'estrategia': estra})

# # Update Views - Unique Item
# # ----------------------------------------------------------------------------
# def visualizarEstrategia(request, estra_id):
#     """View a single strategy."""
#     estra = get_object_or_404(Estrategia, id=estra_id)
#     return render(request, 'visualizar_estrategia.html', {'estrategia': estra})