from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Reporte
from data_models.models import Grupo
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

def visualizarReportes(request):
    """Display all strategies with optional search functionality."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            query = request.GET.get('q', '')
            if query:
                # Search in multiple fields
                reportes = Reporte.objects.filter(
                    Q(nombre__icontains=query) |
                    Q(curso__icontains=query) |
                    Q(anio_escolar__icontains=query) |
                    Q(grupo__icontains=query) |
                    Q(autor__icontains=query)
                )
            else:
                reportes = Reporte.objects.all()
            
            return render(request, 'profesor_principal/listar_reportes.html', {
                'reportes': reportes,
                'query': query
            })
        else:
            messages.error(request, "No tienes permiso para visualizar reportes.")
            return redirect("pagina_principal")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

# Form Views
# ----------------------------------------------------------------------------
def crearReporte(request):
    """Handle report form submission and display."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            grupos = Grupo.objects.all()
            if request.method == 'POST':
                # Extract form data
                form_data = {
                    'grupo': request.POST.get('grupo'),
                    'codigo': request.POST.get('codigo'),
                    'periodo': request.POST.get('periodo'),
                    'fecha': request.POST.get('fecha'),
                    'autor': request.POST.get('autor'),
                    'institucion': request.POST.get('institucion'),
                    'resumen': request.POST.get('resumen'),
                    'objetivos': request.POST.get('objetivos'),
                    'actividades': request.POST.get('actividades'),
                    'resultados': request.POST.get('resultados'),
                    'analisis': request.POST.get('analisis'),
                    'desafios': request.POST.get('desafios'),
                    'proximos_pasos': request.POST.get('proximos_pasos'),
                    'anexos': request.FILES.get('anexos')
                }

                try:
                    reporte = Reporte.objects.create(**form_data)
                    messages.success(request, "Reporte registrado correctamente.")
                    return redirect('reportes')
                except Exception as e:
                    messages.error(request, f"Error al registrar el reporte: {str(e)}")

            return render(request, 'profesor_principal/formular_reporte.html', {"grupos": grupos})
        else:
            messages.error(request, "No tienes permiso para crear reportes.")
            return redirect("pagina_principal")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

# Delete Views - Single Item
# ----------------------------------------------------------------------------
def eliminarReporte(request, reporte_id):
    """Delete a single report."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            reporte = get_object_or_404(Reporte, id=reporte_id)
            reporte.delete()
            messages.success(request, "Reporte eliminado correctamente.")
            return redirect('reportes')
        else:
            messages.error(request, "No tienes permiso para eliminar reportes.")
            return redirect("pagina_principal")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

# Delete Views - Multiple Items
# ----------------------------------------------------------------------------
def eliminarReportes(request):
    """Delete multiple reports."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            if request.method == 'POST':
                reportes_ids = request.POST.getlist('reportes[]')
                if reportes_ids:
                    Reporte.objects.filter(id__in=reportes_ids).delete()
                    messages.success(request, "Reportes eliminados correctamente.")
                else:
                    messages.error(request, "No se seleccionaron reportes para eliminar.")
                return redirect('reportes')
            return JsonResponse({'error': 'Método no permitido'}, status=405)
        else:
            messages.error(request, "No tienes permiso para eliminar reportes.")
            return redirect("pagina_principal")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def modificarReporte(request, reporte_id):
    """Modify a single report."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            reporte = get_object_or_404(Reporte, id=reporte_id)
            
            if request.method == 'POST':
                # Extract form data
                form_data = {
                    'grupo': request.POST.get('grupo'),
                    'codigo': request.POST.get('codigo'),
                    'periodo': request.POST.get('periodo'),
                    'fecha': request.POST.get('fecha'),
                    'autor': request.POST.get('autor'),
                    'institucion': request.POST.get('institucion'),
                    'resumen': request.POST.get('resumen'),
                    'objetivos': request.POST.get('objetivos'),
                    'actividades': request.POST.get('actividades'),
                    'resultados': request.POST.get('resultados'),
                    'analisis': request.POST.get('analisis'),
                    'desafios': request.POST.get('desafios'),
                    'proximos_pasos': request.POST.get('proximos_pasos')
                }

                # Handle file upload if present
                if 'anexos' in request.FILES:
                    form_data['anexos'] = request.FILES['anexos']

                try:
                    # Update report with new data
                    for key, value in form_data.items():
                        setattr(reporte, key, value)
                    reporte.save()
                    messages.success(request, "Reporte actualizado correctamente.")
                    return redirect('reportes')
                except Exception as e:
                    messages.error(request, f"Error al actualizar el reporte: {str(e)}")
                    return render(request, 'modificar_reporte.html', {'reporte': reporte})

            return render(request, 'modificar_reporte.html', {'reporte': reporte})
        else:
            messages.error(request, "No tienes permiso para modificar reportes.")
            return redirect("pagina_principal")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def visualizarReporte(request, reporte_id):
    """View a single strategy."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            reporte = get_object_or_404(Reporte, id=reporte_id)
            return render(request, 'profesor_principal/visualizar__reporte.html', {'reporte': reporte})
        else:
            messages.error(request, "No tienes permiso para visualizar reportes.")
            return redirect("pagina_principal")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")