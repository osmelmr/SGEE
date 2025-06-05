from grupos.models import Grupo
from profesores.models import Profesor  # Ajusta el import según tu proyecto
from django.shortcuts import render, redirect
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
    profesores = Profesor.objects.all()
    profesores_guia = Profesor.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        direccion = request.POST.get('direccion', '').strip()
        curso = request.POST.get('curso', '').strip()
        anio_escolar = request.POST.get('anio_escolar', '').strip()
        caracterizacion = request.POST.get('caracterizacion', '').strip()
        guia_id = request.POST.get('guia')
        profesores_ids = request.POST.getlist('profesores')

        # Validación básica
        if not (nombre and direccion and curso and anio_escolar and caracterizacion and guia_id and profesores_ids):
            messages.error(request, ".")
            return redirect('p_formular_grupo')  # 👍 Esto está bien
        else:
            grupo = Grupo(
                nombre=nombre,
                direccion=direccion,
                curso=curso,
                anio_escolar=anio_escolar,
                caracterizacion=caracterizacion,
                guia_id=guia_id
            )
            grupo.save()
            grupo.profesores.set(profesores_ids)
            messages.success(request, "Grupo creado correctamente.")
            return redirect('p_grupos')
    return render(
        request,
        'profesor_principal/formular_grupo.html',
        {
            'profesores': profesores,
            'profesores_guia': profesores_guia
        }
    )

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
    profesores = Profesor.objects.all()
    profesores_guia = Profesor.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        direccion = request.POST.get('direccion', '').strip()
        curso = request.POST.get('curso', '').strip()
        anio_escolar = request.POST.get('anio_escolar', '').strip()
        caracterizacion = request.POST.get('caracterizacion', '').strip()
        guia_id = request.POST.get('guia')
        profesores_ids = request.POST.getlist('profesores')

        if not (nombre and direccion and curso and anio_escolar and caracterizacion and guia_id and profesores_ids):
            messages.error(request, "Todos los campos son obligatorios.")
        else:
            grupo.nombre = nombre
            grupo.direccion = direccion
            grupo.curso = curso
            grupo.anio_escolar = anio_escolar
            grupo.caracterizacion = caracterizacion
            grupo.guia_id = guia_id
            grupo.save()
            grupo.profesores.set(profesores_ids)
            messages.success(request, "Grupo modificado correctamente.")
            return redirect('p_grupos')
    return render(
        request,
        'profesor_principal/modificar_grupo.html',
        {
            'grupo': grupo,
            'profesores': profesores,
            'profesores_guia': profesores_guia
        }
    )

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