from django.shortcuts import render, get_object_or_404, redirect
from reportes.models import Reporte
from grupos.models import Grupo
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
import os
from django.core.files.base import ContentFile

def visualizar_reportes(request):
    """Display all reports with optional search functionality."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    query = request.GET.get('q', '')
    if query:
        reportes = Reporte.objects.filter(
            Q(grupo__nombre__icontains=query) |  # Buscar por nombre del grupo asociado
            Q(codigo__icontains=query) |
            Q(periodo__icontains=query) |
            Q(autor__icontains=query) |
            Q(institucion__icontains=query) |
            Q(resumen__icontains=query) |
            Q(objetivos__icontains=query) |
            Q(actividades__icontains=query) |
            Q(resultados__icontains=query) |
            Q(analisis__icontains=query) |
            Q(desafios__icontains=query) |
            Q(proximos_pasos__icontains=query)
        )
    else:
        reportes = Reporte.objects.all()
    return render(request, 'profesor_principal/listar_reportes.html', {
        'reportes': reportes,
        'query': query
    })

def crear_reporte(request):
    """Handle report form submission and display."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    grupos = Grupo.objects.all()
    if request.method == 'POST':
        grupo_id = request.POST.get('grupo')
        grupo_instance = Grupo.objects.filter(id=grupo_id).first()
        form_data = {
            'grupo': grupo_instance,
            'periodo': request.POST.get('periodo'),
            'autor': request.POST.get('autor'),
            'institucion': request.POST.get('institucion'),
            'resumen': request.POST.get('resumen'),
            'objetivos': request.POST.get('objetivos'),
            'actividades': request.POST.get('actividades'),
            'resultados': request.POST.get('resultados'),
            'analisis': request.POST.get('analisis'),
            'desafios': request.POST.get('desafios'),
            'proximos_pasos': request.POST.get('proximos_pasos'),
        }

        try:
            # 1. Crear el reporte sin anexos para obtener el id
            reporte = Reporte.objects.create(**form_data)
            # 2. Si hay archivo, renombrar y asignar
            if request.FILES.get('anexos'):
                file = request.FILES['anexos']
                if not file.content_type.startswith('image/'):
                    messages.error(request, "Solo se permiten archivos de imagen (foto).")
                    reporte.delete()  # Limpieza si no es imagen
                    return render(request, 'profesor_principal/formular_reporte.html', {"grupos": grupos})
                ext = os.path.splitext(file.name)[1]
                nuevo_nombre = f"reporte_{reporte.id}_anexo{ext}"
                file_content = ContentFile(file.read())
                reporte.anexos.save(nuevo_nombre, file_content, save=True)
            messages.success(request, "Registro satisfactorio.")
            return redirect('p_reportes')
        except Exception as e:
            messages.error(request, f"Error al registrar el reporte: {str(e)}")

    return render(request, 'profesor_principal/formular_reporte.html', {"grupos": grupos})

def eliminar_reporte(request, reporte_id):
    """Delete a single report."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    reporte = get_object_or_404(Reporte, id=reporte_id)
    reporte.delete()
    messages.success(request, "Eliminación satisfactoria.")
    return redirect('p_reportes')

def eliminar_reportes(request):
    """Delete multiple reports."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    if request.method == 'POST':
        reportes_ids = request.POST.getlist('reportes[]')
        if reportes_ids:
            Reporte.objects.filter(id__in=reportes_ids).delete()
            messages.success(request, "Eliminación satisfactoria.")
        else:
            messages.error(request, "No se seleccionaron reportes para eliminar.")
        return redirect('p_reportes')
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def modificar_reporte(request, reporte_id):
    """Modify a single report."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    reporte = get_object_or_404(Reporte, id=reporte_id)
    grupos = Grupo.objects.all()
    if request.method == 'POST':
        form_data = {
            'grupo': request.POST.get('grupo'),
            'periodo': request.POST.get('periodo'),
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
        if 'anexos' in request.FILES:
            file = request.FILES['anexos']
            if not file.content_type.startswith('image/'):
                messages.error(request, "Solo se permiten archivos de imagen (foto).")
                return render(request, 'profesor_principal/modificar_reporte.html', {'reporte': reporte})
            form_data['anexos'] = file

        try:
            for key, value in form_data.items():
                setattr(reporte, key, value)
            reporte.save()
            messages.success(request, "Modificación satisfactoria.")
            return redirect('p_reportes')
        except Exception as e:
            messages.error(request, f"Error al actualizar el reporte: {str(e)}")
            return render(request, 'profesor_principal/modificar_reporte.html', {'reporte': reporte, 'grupos': grupos})

    return render(request, 'profesor_principal/modificar_reporte.html', {'reporte': reporte, 'grupos': grupos})

def visualizar_reporte(request, reporte_id):
    """View a single strategy."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para funcion modelo.")
        return redirect("pagina_principal")
    reporte = get_object_or_404(Reporte, id=reporte_id)
    return render(request, 'profesor_principal/visualizar_reporte.html', {'reporte': reporte})