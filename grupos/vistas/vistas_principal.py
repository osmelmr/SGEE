from data_models.forms import GrupoForm
from django.shortcuts import render, redirect
from data_models.models import Grupo
from django.contrib import messages
from django.db.models import Q

def crearGrupo(request):
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
            return redirect('profesor_principal/listar_grupos')
    else:
        form = GrupoForm()
    return render(request, 'profesor_principal/formular_grupo.html', {'form': form})

def visualizarGrupo(request, grupo_id):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para visualizar grupos.")
        return redirect("pagina_principal")
    grupo = Grupo.objects.get(id=grupo_id)
    return render(request, 'profesor_principal/visualizar_grupo.html', {'grupo': grupo})

def modificarGrupo(request, grupo_id):
    if not request.user.is_authenticated:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    if not request.user.es_profesor():
        messages.error(request, "No tienes permiso para modificar grupos.")
        return redirect("pagina_principal")
    grupo = Grupo.objects.get(id=grupo_id)
    return render(request, 'profesor_principal/modificar_grupo.html', {'grupo': grupo})

def listarGrupos(request):
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