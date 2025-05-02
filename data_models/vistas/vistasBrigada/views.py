from data_models.forms import BrigadaForm
from django.shortcuts import render, redirect
from data_models.models import Brigada

def crearBrigada(request):
    if request.method == 'POST':
        form = BrigadaForm(request.POST)
        if form.is_valid():
            brigada = form.save(commit=False)
            brigada.save()
            form.save_m2m()
            return redirect('listar_brigadas')
    else:
        form = BrigadaForm()
    return render(request, 'brigada_form.html', {'form': form})

def visualizarBrigada(request, brigada_id):
    
    brigada = Brigada.objects.get(id=brigada_id)
    return render(request, 'brigada_detail.html', {'brigada': brigada})

def listarBrigadas(request):
    brigadas = Brigada.objects.all()
    return render(request, 'brigada_list.html', {'brigadas': brigadas})