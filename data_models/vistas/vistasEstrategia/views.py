from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Estrategia, Grupo
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
import json
from django.http import HttpResponse
from docx import Document
from io import BytesIO
from django.db.models import OneToOneField
from django.template.loader import render_to_string
from xhtml2pdf import pisa

def visualizarEstrategias(request):
    """Display all strategies with optional search functionality."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            query = request.GET.get("q", "")
            if query:
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
        else:
            messages.error(request, "No tienes permiso para visualizar estrategias.")
            return redirect("pagina_principal")
    else:
        messages.error(request, "No estás autenticado.")
        return redirect("login")

# Form Views
# ----------------------------------------------------------------------------
def crearEstrategia(request):
    """Handle strategy form submission and display."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
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
                grupo_escogido = Grupo.objects.get(nombre=request.POST.get("grupo"))
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
                    "grupo_id": grupo_escogido,  # Set the group ID
                }
                try:
                    Estrategia.objects.create(**form_data)
                    messages.success(request, "Estrategia registrada correctamente.")
                    return redirect("estrategias")
                except Exception as e:
                    messages.error(request, f"Error al registrar la estrategia: {str(e)}")
                    return render(request, "profesor_principal/formular_estrategia.html", {
                        "grupos": grupos,
                        "grupos_json": grupos_json
                    })
            
            return render(request, "profesor_principal/formular_estrategia.html", {
                "grupos": grupos,
                "grupos_json": grupos_json
            })
        else:
            messages.error(request, "No tienes permiso para crear estrategias.")
            return redirect("estrategias")
    else:
        messages.error(request, "No estás autenticado.")
        return redirect("login")

# Delete Views - Single Item
# ----------------------------------------------------------------------------
def eliminarEstrategia(request, estra_id):
    """Delete a single strategy."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            estra = get_object_or_404(Estrategia, id=estra_id)
            estra.delete()
            messages.success(request, "Estrategia eliminada correctamente.")
            return redirect("estrategias")
        else:
            messages.error(request, "No tienes permiso para eliminar estrategias.")
            return redirect("estrategias")
    else:
        messages.error(request, "No estás autenticado.")
        return redirect("login")

# Delete Views - Multiple Items
# ----------------------------------------------------------------------------
def eliminarEstrategias(request):
    """Delete multiple strategies."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            if request.method == "POST":
                estrategias_ids = request.POST.getlist("estrategias[]")
                if estrategias_ids:
                    Estrategia.objects.filter(id__in=estrategias_ids).delete()
                    messages.success(request, "Estrategias eliminadas correctamente.")
                else:
                    messages.error(request, "No se seleccionaron estrategias para eliminar.")
                return redirect("estrategias")
            return JsonResponse({"error": "Método no permitido"}, status=405)
        else:
            messages.error(request, "No tienes permiso para eliminar estrategias.")
            return redirect("estrategias")
    else:
        messages.error(request, "No estás autenticado.")
        return redirect("login")

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def modificarEstrategia(request, estra_id):
    if request.user.is_authenticated:
        if request.user.es_profesor():
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
                    print(str(e))
                    messages.error(request, f"Error al modificar la estrategia: {str(e)}")
                    return render(request, "profesor_principal/modificar_estrategia.html", {"estrategia": estra})
            return render(request, "profesor_principal/modificar_estrategia.html", {"estrategia": estra})
        else:
            messages.error(request, "No tienes permiso para modificar estrategias.")
            return redirect("estrategias")
    else:
        messages.error(request, "No estás autenticado.")
        return redirect("login")

# Update Views - Unique Item
# ----------------------------------------------------------------------------
def visualizarEstrategia(request, estra_id):
    """View a single strategy."""
    if request.user.is_authenticated:
        if request.user.es_profesor():
            estra = get_object_or_404(Estrategia, id=estra_id)
            return render(request, "profesor_principal/visualizar_estrategia.html", {"estrategia": estra})
        else:
            messages.error(request, "No tienes permiso para visualizar estrategias.")
            return redirect("pagina_principal")
    else:
        messages.error(request, "No estás autenticado.")
        return redirect("login")
    

def estrategia_docx(request, id):
    # Obtener la instancia de Estrategia
    estrategia = get_object_or_404(Estrategia, id=id)

    # Crear documento Word en memoria
    doc = Document()
    for field in Estrategia._meta.fields:
        # Omitir campo one-to-one (grupo)
        if isinstance(field, OneToOneField):
            continue
        # Obtener valor del campo
        value = getattr(estrategia, field.name)
        # Agregar párrafo con "nombre del campo: valor"
        doc.add_paragraph(f"{field.verbose_name}: {value}")

    # Guardar documento en un buffer en memoria
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    # Preparar respuesta como archivo adjunto
    response = HttpResponse(
        buffer.getvalue(),
        content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    response['Content-Disposition'] = f'attachment; filename="estrategia_{estrategia.id}.docx"'
    return response


def estrategia_pdf(request, estra_id):
    if request.user.is_authenticated:
        estrategia = get_object_or_404(Estrategia, id=estra_id)

        # Renderizar HTML
        html = render_to_string("estrategia_pdf.html", {'estrategia': estrategia})

        # Generar PDF desde HTML
        buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=buffer)
        buffer.seek(0)

        if pisa_status.err:
            return HttpResponse("Error al generar el PDF", status=500)

        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{estrategia.nombre}_{estrategia.id}.pdf"'
        return response
    else:
        messages.error(request, "No estás autenticado.")
        return redirect("login")
