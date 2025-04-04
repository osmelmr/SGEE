from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Reporte
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

def visualizarReportes(request):
    """Display all strategies with optional search functionality."""
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
    
    return render(request, 'reportes.html', {
        'reportes': reportes,
        'query': query
    })

# Form Views
# ----------------------------------------------------------------------------
def crearReporte(request):
    """Handle report form submission and display."""
    if request.method == 'POST':
        # Extract form data
        form_data = {
            'brigada': request.POST.get('brigada'),
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
            'proximos_pasos': request.POST.get('proximos-pasos'),
            'anexos': request.FILES.get('anexos')
        }

        try:
            reporte = Reporte(**form_data)
            reporte.save()
            messages.success(request, "Reporte registrado correctamente.")
            return redirect('reportes')
        except Exception as e:
            messages.error(request, f"Error al registrar el reporte: {str(e)}")

    return render(request, 'formulario_reporte.html')

# Delete Views - Single Item
# ----------------------------------------------------------------------------
def eliminarReporte(request, reporte_id):
    """Delete a single report."""
    reporte = get_object_or_404(Reporte, id=reporte_id)
    reporte.delete()
    messages.success(request, "Reporte eliminado correctamente.")
    return redirect('reportes')

# Delete Views - Multiple Items
# ----------------------------------------------------------------------------
def eliminarReportes(request):
    """Delete multiple reports."""
    if request.method == 'POST':
        reportes_ids = request.POST.getlist('reportes[]')
        if reportes_ids:
            Reporte.objects.filter(id__in=reportes_ids).delete()
            messages.success(request, "Reportes eliminados correctamente.")
        else:
            messages.error(request, "No se seleccionaron reportes para eliminar.")
        return redirect('reportes')
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def modificarReporte(request, estra_id):
    """Modify a single strategy."""
    estra = get_object_or_404(Reporte, id=estra_id)
    return render(request, 'modificar_reporte.html', {'reporte': estra})

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def visualizarReporte(request, estra_id):
    """View a single strategy."""
    estra = get_object_or_404(Reporte, id=estra_id)
    return render(request, 'visualizar_reporte.html', {'reporte': estra})