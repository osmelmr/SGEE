from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Encuesta
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

def visualizarEncuestas(request):
    """Display all strategies with optional search functionality."""
    query = request.GET.get('q', '')
    if query:
        # Search in multiple fields
        encuestas = Encuesta.objects.filter(
            Q(nombre__icontains=query) |
            Q(curso__icontains=query) |
            Q(anio_escolar__icontains=query) |
            Q(grupo__icontains=query) |
            Q(autor__icontains=query)
        )
    else:
        encuestas = Encuesta.objects.all()
    
    return render(request, 'profesor_principal/listar_encuestas.html', {
        'encuestas': encuestas,
        'query': query
    })

# Form Views
# ----------------------------------------------------------------------------
def crearEncuesta(request):
    """Handle survey form submission and display."""
    if request.method == 'POST':
        # Extract data from the form
        form_data = {
            'titulo': request.POST.get('titulo'),
            'descripcion': request.POST.get('descripcion'),
            'autor': request.POST.get('autor'),
            'estado': request.POST.get('estado')
        }
        
        try:
            encuesta = Encuesta.objects.create(**form_data)
            # Save associated questions
            preguntas = request.POST.getlist('preguntas[]')
            for texto in preguntas:
                if texto.strip():
                    encuesta.preguntas.create(texto=texto)
            messages.success(request, "Encuesta registrada correctamente.")
            return redirect('encuestas')
        except Exception as e:
            messages.error(request, f"Error al registrar la encuesta: {str(e)}")
    
    return render(request, 'profesor_principal/formular_encuesta.html')

# Delete Views - Single Item
# ----------------------------------------------------------------------------
def eliminarEncuesta(request, encuesta_id):
    """Delete a single survey."""
    encuesta = get_object_or_404(Encuesta, id=encuesta_id)
    encuesta.delete()
    messages.success(request, "Encuesta eliminada correctamente.")
    return redirect('encuestas')

# Delete Views - Multiple Items
# ----------------------------------------------------------------------------
def eliminarEncuestas(request):
    """Delete multiple strategies."""
    if request.method == 'POST':
        encuestas_ids = request.POST.getlist('encuestas[]')
        if encuestas_ids:
            Encuesta.objects.filter(id__in=encuestas_ids).delete()
            messages.success(request, "Encuestas eliminadas correctamente.")
        else:
            messages.error(request, "No se seleccionaron encuestas para eliminar.")
        return redirect('encuestas')
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def modificarEncuesta(request, encuesta_id):
    """Modify a single survey."""
    encuesta = get_object_or_404(Encuesta, id=encuesta_id)
    
    if request.method == 'POST':
        # Extract form data
        form_data = {
            'titulo': request.POST.get('titulo'),
            'descripcion': request.POST.get('descripcion'),
            'autor': request.POST.get('autor'),
            'estado': request.POST.get('estado')
        }

        try:
            # Update survey with new data
            for key, value in form_data.items():
                setattr(encuesta, key, value)
            encuesta.save()

            # Handle questions
            preguntas = request.POST.getlist('preguntas[]')
            encuesta.preguntas.all().delete()
            for texto in preguntas:
                if texto.strip():
                    encuesta.preguntas.create(texto=texto)

            messages.success(request, "Encuesta actualizada correctamente.")
            return redirect('encuestas')
        except Exception as e:
            messages.error(request, f"Error al actualizar la encuesta: {str(e)}")
            return render(request, 'modificar_encuesta.html', {'encuesta': encuesta})

    return render(request, 'modificar_encuesta.html', {'encuesta': encuesta})

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def visualizarEncuesta(request, encuesta_id):
    """View a single strategy."""
    encuesta = get_object_or_404(Encuesta, id=encuesta_id)
    return render(request, 'profesor_principal/visualizar__encuesta.html', {'encuesta': encuesta})