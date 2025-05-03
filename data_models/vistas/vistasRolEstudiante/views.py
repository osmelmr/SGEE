from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Reporte
from data_models.models import Grupo
from data_models.models import Estrategia
from data_models.models import Evento
from data_models.models import Profesor

def visualizarEstrategiasE(request):
    estrategias=Estrategia.objects.all()
    return render(request, "plantillas_estudiantes/estrategias_estudiante.html", {"estrategias":estrategias})