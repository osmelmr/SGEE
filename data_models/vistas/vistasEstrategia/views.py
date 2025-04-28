from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Estrategia, Brigada
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
import json

def visualizarEstrategias(request):
    """Display all strategies with optional search functionality."""
    query = request.GET.get("q", "")
    if query:
        # Search in multiple fields
        estrategias = Estrategia.objects.filter(
            Q(nombre__icontains=query) |
            Q(curso__icontains=query) |
            Q(anio_escolar__icontains=query) |
            Q(grupo__icontains=query) |
            Q(autor__icontains=query)
        )
    else:
        estrategias = Estrategia.objects.all()
    
    return render(request, "estrategias.html", {
        "estrategias": estrategias,
        "query": query
    })

# Form Views
# ----------------------------------------------------------------------------
def crearEstrategia(request):
    """Handle strategy form submission and display."""
    from data_models.models import Brigada  # Asegúrate de importar Brigada

    brigadas = Brigada.objects.all()  # Obtén todas las brigadas
    brigadas_json = json.dumps([
        {
            "id": brigada.id,
            "nombre": brigada.nombre,
            "direccion": brigada.direccion,
            "curso": brigada.curso,
            "anio_escolar":brigada.anio_escolar,
            "caracterizacion": brigada.caracterizacion
        }
        for brigada in brigadas
    ])

    if request.method == "POST":
        # Extract form data
        form_data = {
            "nombre": request.POST.get("titulo-estrategia"),
            "curso": request.POST.get("curso"),
            "anio_escolar": request.POST.get("ano-escolar"),
            "grupo": request.POST.get("grupo"),
            "plan_estudios": request.POST.get("plan-estudios"),
            "obj_estrategia": request.POST.get("objetivos-estrategia"),
            "dir_brigada": request.POST.get("direccion-brigada"),
            "caract_brigada": request.POST.get("caracteristicas-brigada"),
            "colect_pedagogico": request.POST.get("colectivo-pedagogico"),
            "otros_aspectos": request.POST.get("otros-aspectos", "otros_aspectos"),
            "dim_curricular": request.POST.get("dimension-curricular"),
            "dim_extensionista": request.POST.get("dimension-extensionista"),
            "dim_politica": request.POST.get("dimension-politico-ideologica"),
            "conclusiones": request.POST.get("conclusiones"),
            "obj_general": request.POST.get("objetivo-general"),
            "obj_dc": request.POST.get("objetivos-especificos-curricular"),
            "plan_dc": request.POST.get("plan-acciones-curricular"),
            "obj_de": request.POST.get("objetivos-especificos-extensionista"),
            "plan_de": request.POST.get("plan-acciones-extensionista"),
            "obj_dp": request.POST.get("objetivos-especificos-politico-ideologica"),
            "plan_dp": request.POST.get("plan-acciones-politico-ideologica"),
            "evaluacion": request.POST.get("evaluacion-integral"),
            "autor": request.POST.get("autor"),
        }
        
        try:
            estrategia = Estrategia(**form_data)
            estrategia.save()
            messages.success(request, "Estrategia registrada correctamente.")
            return redirect("estrategias")
        except Exception as e:
            messages.error(request, f"Error al registrar la estrategia: {str(e)}")
            # Si hay error, vuelve a mostrar el formulario con las brigadas
            return render(request, "formulario_estrategia.html", {
                "brigadas": brigadas,
                "brigadas_json": brigadas_json
            })
    
    # GET: mostrar formulario con las brigadas y datos para autocompletar
    return render(request, "formulario_estrategia.html", {
        "brigadas": brigadas,
        "brigadas_json": brigadas_json
    })

# Delete Views - Single Item
# ----------------------------------------------------------------------------
def eliminarEstrategia(request, estra_id):
    """Delete a single strategy."""
    estra = get_object_or_404(Estrategia, id=estra_id)
    estra.delete()
    messages.success(request, "Estrategia eliminada correctamente.")
    return redirect("estrategias")

# Delete Views - Multiple Items
# ----------------------------------------------------------------------------
def eliminarEstrategias(request):
    """Delete multiple strategies."""
    if request.method == "POST":
        estrategias_ids = request.POST.getlist("estrategias[]")
        if estrategias_ids:
            Estrategia.objects.filter(id__in=estrategias_ids).delete()
            messages.success(request, "Estrategias eliminadas correctamente.")
        else:
            messages.error(request, "No se seleccionaron estrategias para eliminar.")
        return redirect("estrategias")
    return JsonResponse({"error": "Método no permitido"}, status=405)

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def modificarEstrategia(request, estra_id):
    """Modify a single strategy."""
    estra = get_object_or_404(Estrategia, id=estra_id)
    
    if request.method == "POST":
        # Extraer datos del formulario
        form_data = {
            "nombre": request.POST.get("titulo-estrategia"),
            "curso": request.POST.get("curso"),
            "anio_escolar": request.POST.get("ano-escolar"),
            "grupo": request.POST.get("grupo"),
            "plan_estudios": request.POST.get("plan-estudios"),
            "obj_estrategia": request.POST.get("objetivos-estrategia"),
            "dir_brigada": request.POST.get("direccion-brigada"),
            "caract_brigada": request.POST.get("caracteristicas-brigada"),
            "colect_pedagogico": request.POST.get("colectivo-pedagogico"),
            "otros_aspectos": request.POST.get("otros-aspectos"),
            "dim_curricular": request.POST.get("dimension-curricular"),
            "dim_extensionista": request.POST.get("dimension-extensionista"),
            "dim_politica": request.POST.get("dimension-politico-ideologica"),
            "conclusiones": request.POST.get("conclusiones"),
            "obj_general": request.POST.get("objetivo-general"),
            "obj_dc": request.POST.get("objetivos-especificos-curricular"),
            "plan_dc": request.POST.get("plan-acciones-curricular"),
            "obj_de": request.POST.get("objetivos-especificos-extensionista"),
            "plan_de": request.POST.get("plan-acciones-extensionista"),
            "obj_dp": request.POST.get("objetivos-especificos-politico-ideologica"),
            "plan_dp": request.POST.get("plan-acciones-politico-ideologica"),
            "evaluacion": request.POST.get("evaluacion-integral"),
            "autor": request.POST.get("autor"),
        }
        
        try:
            # Actualizar cada campo de la estrategia
            for field, value in form_data.items():
                setattr(estra, field, value)
            
            # Guardar los cambios
            estra.save()
            messages.success(request, "Estrategia modificada correctamente.")
            return redirect("estrategias")
        except Exception as e:
            messages.error(request, f"Error al modificar la estrategia: {str(e)}")
            return render(request, "modificar_estrategia.html", {"estrategia": estra})
    
    # Si es GET, mostrar el formulario con los datos actuales
    return render(request, "modificar_estrategia.html", {"estrategia": estra})

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def visualizarEstrategia(request, estra_id):
    """View a single strategy."""
    estra = get_object_or_404(Estrategia, id=estra_id)
    return render(request, "visualizar_estrategia.html", {"estrategia": estra})