from django.shortcuts import render, get_object_or_404, redirect
from encuestas.models import  Encuesta
from django.contrib import messages
from encuestas.models import Respuesta, Pregunta
from django.db.models import Q

def visualizar_encuestas(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar solo las encuestas que el usuario no ha realizado y que están activas."""
    usuario = request.user
    encuestas_realizadas = usuario.encuestas_realizadas.all()
    query = request.GET.get("q", "")
    base_queryset = Encuesta.objects.filter(estado='activa').exclude(id__in=encuestas_realizadas.values_list('id', flat=True))
    if query:
        encuestas = base_queryset.filter(
            Q(titulo__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(autor__icontains=query) |
            Q(estado__icontains=query)
        )
    else:
        encuestas = base_queryset
    return render(request, "usuarios/listar_encuestas.html", {"encuestas": encuestas, "query": query})

def visualizar_encuesta(request, encuesta_id):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')
    """Visualizar una encuesta específica."""
    encuesta = get_object_or_404(Encuesta, id=encuesta_id)
    return render(request, "usuarios/visualizar_encuesta.html", {"encuesta": encuesta})

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
        return redirect('encuestas')

    return render(request, 'usuarios/realizar_encuesta.html', {
        'encuesta': encuesta,
        'preguntas': preguntas,
    })