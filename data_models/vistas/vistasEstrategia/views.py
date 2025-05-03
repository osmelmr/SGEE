from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Estrategia, Grupo
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
import json
from django.contrib.auth.decorators import user_passes_test, login_required

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
    
    return render(request, "profesor_principal/listar_estrategias.html", {
        "estrategias": estrategias,
        "query": query
    })

# Form Views
# ----------------------------------------------------------------------------
def crearEstrategia(request):
    """Handle strategy form submission and display."""
    grupos = Grupo.objects.all()
    grupos_json = json.dumps([
        {
            "id": grupo.id,
            "nombre": grupo.nombre,
            "direccion": grupo.direccion,
            "curso": grupo.curso,
            "anio_escolar": grupo.anio_escolar,
            "caracterizacion": grupo.caracterizacion
        }
        for grupo in grupos
    ])

    if request.method == "POST":
        # Extract form data
        form_data = {
            "nombre": request.POST.get("nombre"),
            "curso": request.POST.get("curso"),
            "anio_escolar": request.POST.get("anio_escolar"),
            "grupo": request.POST.get("grupo"),
            "plan_estudios": request.POST.get("plan_estudios"),
            "obj_estrategia": request.POST.get("obj_estrategia"),
            "dir_grupo": request.POST.get("dir_grupo"),
            "caract_grupo": request.POST.get("caract_grupo"),
            "colect_pedagogico": request.POST.get("colect_pedagogico"),
            "otros_aspectos": request.POST.get("otros_aspectos"),
            "dim_curricular": request.POST.get("dim_curricular"),
            "dim_extensionista": request.POST.get("dim_extensionista"),
            "dim_politica": request.POST.get("dim_politica"),
            "conclusiones": request.POST.get("conclusiones"),
            "obj_general": request.POST.get("obj_general"),
            "obj_dc": request.POST.get("obj_dc"),
            "plan_dc": request.POST.get("plan_dc"),
            "obj_de": request.POST.get("obj_de"),
            "plan_de": request.POST.get("plan_de"),
            "obj_dp": request.POST.get("obj_dp"),
            "plan_dp": request.POST.get("plan_dp"),
            "evaluacion": request.POST.get("evaluacion"),
            "autor": request.POST.get("autor"),
        }
        try:
            estrategia = Estrategia.objects.create(**form_data)
            messages.success(request, "Estrategia registrada correctamente.")
            return redirect("estrategias")
        except Exception as e:
            print(str(e))
            messages.error(request, f"Error al registrar la estrategia: {str(e)}")
            return render(request, "profesor_principal/formular_estrategia.html", {
                "grupos": grupos,
                "grupos_json": grupos_json
            })
    
    return render(request, "profesor_principal/formular_estrategia.html", {
        "grupos": grupos,
        "grupos_json": grupos_json
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
@login_required
@user_passes_test(lambda u: u.es_profesor(), login_url='/login/')
def modificarEstrategia(request, estra_id):
    """Modify a single strategy."""
    estra = get_object_or_404(Estrategia, id=estra_id)
    
    if request.method == "POST":
        # Extract form data
        form_data = {
            "nombre": request.POST.get("nombre"),
            "curso": request.POST.get("curso"),
            "anio_escolar": request.POST.get("anio_escolar"),
            "grupo": request.POST.get("grupo"),
            "plan_estudios": request.POST.get("plan_estudios"),
            "obj_estrategia": request.POST.get("obj_estrategia"),
            "dir_grupo": request.POST.get("dir_grupo"),
            "caract_grupo": request.POST.get("caract_grupo"),
            "colect_pedagogico": request.POST.get("colect_pedagogico"),
            "otros_aspectos": request.POST.get("otros_aspectos"),
            "dim_curricular": request.POST.get("dim_curricular"),
            "dim_extensionista": request.POST.get("dim_extensionista"),
            "dim_politica": request.POST.get("dim_politica"),
            "conclusiones": request.POST.get("conclusiones"),
            "obj_general": request.POST.get("obj_general"),
            "obj_dc": request.POST.get("obj_dc"),
            "plan_dc": request.POST.get("plan_dc"),
            "obj_de": request.POST.get("obj_de"),
            "plan_de": request.POST.get("plan_de"),
            "obj_dp": request.POST.get("obj_dp"),
            "plan_dp": request.POST.get("plan_dp"),
            "evaluacion": request.POST.get("evaluacion"),
            "autor": request.POST.get("autor"),
        }
        
        try:
            for field, value in form_data.items():
                setattr(estra, field, value)
            estra.save()
            messages.success(request, "Estrategia modificada correctamente.")
            return redirect("estrategias")
        except Exception as e:
            messages.error(request, f"Error al modificar la estrategia: {str(e)}")
            return render(request, "profesor_principal/modificar_estrategia.html", {"estrategia": estra})
    
    return render(request, "profesor_principal/modificar_estrategia.html", {"estrategia": estra})

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def visualizarEstrategia(request, estra_id):
    """View a single strategy."""
    estra = get_object_or_404(Estrategia, id=estra_id)
    return render(request, "profesor_principal/visualizar_estrategia.html", {"estrategia": estra})