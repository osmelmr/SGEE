from data_models.forms import GrupoForm
from django.shortcuts import render, redirect
from data_models.models import Grupo

def crearGrupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.save()
            form.save_m2m()
            return redirect('profesor_principal/listar_grupos')
    else:
        form = GrupoForm()
    return render(request, 'grupo_form.html', {'form': form})

def visualizarGrupo(request, grupo_id):
    
    grupo = Grupo.objects.get(id=grupo_id)
    return render(request, 'grupo_detail.html', {'grupo': grupo})

def listarGrupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'grupo_list.html', {'grupos': grupos})