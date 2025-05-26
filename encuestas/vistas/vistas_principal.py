from django.shortcuts import render, get_object_or_404, redirect
from encuestas.models import Encuesta
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q


def visualizarEncuestas(request):
    """Display all surveys with optional search functionality."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para visualizar encuestas.")
        return redirect("pagina_principal")
    query = request.GET.get('q', '')
    if query:
        encuestas = Encuesta.objects.filter(
            Q(titulo__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(autor__icontains=query) |
            Q(estado__icontains=query)
        )
    else:
        encuestas = Encuesta.objects.all()
    return render(request, 'profesor_principal/listar_encuestas.html', {
        'encuestas': encuestas,
        'query': query
    })

def crearEncuesta(request):
    """Handle survey form submission and display."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para crear encuestas.")
        return redirect("pagina_principal")
    if request.method == 'POST':
        form_data = {
            'titulo': request.POST.get('titulo'),
            'descripcion': request.POST.get('descripcion'),
            'autor': request.POST.get('autor'),
            'estado': request.POST.get('estado')
        }
        try:
            encuesta = Encuesta.objects.create(**form_data)
            preguntas = request.POST.getlist('preguntas[]')
            for texto in preguntas:
                if texto.strip():
                    encuesta.preguntas.create(texto=texto)
            messages.success(request, "Encuesta registrada correctamente.")
            return redirect('encuestas')
        except Exception as e:
            messages.error(request, f"Error al registrar la encuesta: {str(e)}")
    return render(request, 'profesor_principal/formular_encuesta.html')

def eliminarEncuesta(request, encuesta_id):
    """Delete a single survey."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para eliminar encuestas.")
        return redirect("pagina_principal")
    encuesta = get_object_or_404(Encuesta, id=encuesta_id)
    encuesta.delete()
    messages.success(request, "Encuesta eliminada correctamente.")
    return redirect('encuestas')

def eliminarEncuestas(request):
    """Delete multiple strategies."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para eliminar encuestas.")
        return redirect("pagina_principal")
    if request.method == 'POST':
        encuestas_ids = request.POST.getlist('encuestas[]')
        if encuestas_ids:
            Encuesta.objects.filter(id__in=encuestas_ids).delete()
            messages.success(request, "Encuestas eliminadas correctamente.")
        else:
            messages.error(request, "No se seleccionaron encuestas para eliminar.")
        return redirect('encuestas')
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def modificarEncuesta(request, encuesta_id):
    """Modify a single survey."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para modificar encuestas.")
        return redirect("pagina_principal")
    encuesta = get_object_or_404(Encuesta, id=encuesta_id)
    if request.method == 'POST':
        form_data = {
            'titulo': request.POST.get('titulo'),
            'descripcion': request.POST.get('descripcion'),
            'autor': request.POST.get('autor'),
            'estado': request.POST.get('estado')
        }
        try:
            for key, value in form_data.items():
                setattr(encuesta, key, value)
            encuesta.save()
            preguntas = request.POST.getlist('preguntas[]')
            encuesta.preguntas.all().delete()
            for texto in preguntas:
                if texto.strip():
                    encuesta.preguntas.create(texto=texto)
            messages.success(request, "Encuesta actualizada correctamente.")
            return redirect('encuestas')
        except Exception as e:
            messages.error(request, f"Error al actualizar la encuesta: {str(e)}")
            return render(request, 'profesor_principal/modificar_encuesta.html', {'encuesta': encuesta})
    return render(request, 'profesor_principal/modificar_encuesta.html', {'encuesta': encuesta})

def visualizarEncuesta(request, encuesta_id):
    """View a single strategy."""
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para visualizar encuestas.")
        return redirect("pagina_principal")
    encuesta = get_object_or_404(Encuesta, id=encuesta_id)
    return render(request, 'profesor_principal/visualizar_encuesta.html', {'encuesta': encuesta})


