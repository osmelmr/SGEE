from grupos.forms import GrupoForm
from django.shortcuts import render, redirect
from grupos.models import Grupo
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

def crear_grupo(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para crear grupos.")
        return redirect("pagina_principal")
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.save()
            form.save_m2m()
            return redirect('p_grupos')
    else:
        form = GrupoForm()
    return render(request, 'profesor_principal/formular_grupo.html', {'form': form})

def visualizar_grupo(request, grupo_id):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para visualizar grupos.")
        return redirect("pagina_principal")
    grupo = Grupo.objects.get(id=grupo_id)
    return render(request, 'profesor_principal/visualizar_grupo.html', {'grupo': grupo})

def modificar_grupo(request, grupo_id):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para modificar grupos.")
        return redirect("pagina_principal")
    grupo = Grupo.objects.get(id=grupo_id)
    return render(request, 'profesor_principal/modificar_grupo.html', {'grupo': grupo})

def listar_grupos(request):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para listar grupos.")
        return redirect("pagina_principal")
    query = request.GET.get('q', '')
    if query:
        grupos = Grupo.objects.filter(
            Q(nombre__icontains=query) |
            Q(direccion__icontains=query) |
            Q(curso__icontains=query) |
            Q(anio_escolar__icontains=query) |
            Q(caracterizacion__icontains=query)
        )
    else:
        grupos = Grupo.objects.all()
    return render(request, 'profesor_principal/listar_grupos.html', {'grupos': grupos, 'query': query})

def eliminar_grupo(request, grupo_id):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para eliminar grupos.")
        return redirect("pagina_principal")
    grupo = Grupo.objects.filter(id=grupo_id).first()
    if grupo:
        grupo.delete()
        messages.success(request, "Grupo eliminado correctamente.")
    else:
        messages.error(request, "El grupo no existe.")
    return redirect('p_grupos')

def eliminar_grupos(request, grupo_id=None):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para eliminar grupos.")
        return redirect("pagina_principal")
    if request.method == "POST":
        grupos_ids = request.POST.getlist("grupos[]")
        if grupos_ids:
            Grupo.objects.filter(id__in=grupos_ids).delete()
            messages.success(request, "Grupos eliminados correctamente.")
        else:
            messages.error(request, "No se seleccionaron grupos para eliminar.")
        return redirect('p_grupos')
    return JsonResponse({"error": "Método no permitido"}, status=405)