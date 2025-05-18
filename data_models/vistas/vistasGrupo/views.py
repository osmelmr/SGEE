from data_models.forms import GrupoForm
from django.shortcuts import render, redirect
from data_models.models import Grupo
from django.contrib import messages

def crearGrupo(request):
    if request.user.is_authenticated:
        if request.user.es_profesor():
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
        else:
            messages.error(request, "No tienes permiso para crear grupos.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

def visualizarGrupo(request, grupo_id):
    if request.user.is_authenticated:
        if request.user.es_profesor():
            grupo = Grupo.objects.get(id=grupo_id)
            return render(request, 'profesor_principal/visualizar_grupo.html', {'grupo': grupo})
        else:
            messages.error(request, "No tienes permiso para visualizar grupos.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")
    
def modificarGrupo(request, grupo_id):
    if request.user.is_authenticated:
        if request.user.es_profesor():
            grupo = Grupo.objects.get(id=grupo_id)
            return render(request, 'profesor_principal/modificar_grupo.html', {'grupo': grupo})
        else:
            messages.error(request, "No tienes permiso para visualizar grupos.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")

def listarGrupos(request):
    if request.user.is_authenticated:
        if request.user.es_profesor():
            grupos = Grupo.objects.all()
            return render(request, 'profesor_principal/listar_grupos.html', {'grupos': grupos})
        else:
            messages.error(request, "No tienes permiso para listar grupos.")
            return redirect("pagina_principal_g")
    else:
        messages.error(request, "No estas autenticado.")
        return redirect("login")