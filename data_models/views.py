from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages  # Para retroalimentación al usuario
from .models import Estrategia, Evento, Profesor, Reporte, RegistroUsuario, Encuesta, Pregunta
from .forms import EstrategiaForm, EventoForm, ProfesorForm, ReporteForm, RegistroUsuarioForm, EncuestaForm

# Create your views here.
# Estrategias
def estrategia_list(request):
    estrategias = Estrategia.objects.all()
    context = {'estrategias': estrategias}
    return render(request, 'estrategias.html', context)


def estrategia_detail(request, pk):
    estrategia = get_object_or_404(Estrategia, pk=pk)
    context = {'estrategia': estrategia}
    return render(request, 'estrategia_detail.html', context)


def estrategia_create(request):
    if request.method == 'POST':
        form = EstrategiaForm(request.POST)
        if form.is_valid():
            form.save()
            # Agregar mensaje de éxito
            messages.success(request, "Estrategia registrada correctamente.")
            return redirect('estrategia_list')
        else:
            # Agregar mensaje de error en caso de datos inválidos
            messages.error(request, "Hubo un error al registrar la estrategia. Por favor revisa los datos ingresados.")
    else:
        form = EstrategiaForm()
    context = {'form': form}
    return render(request, 'formulario_estrategia.html', context)

def estrategia_update(request, pk):
    estrategia = get_object_or_404(Estrategia, pk=pk)
    if request.method == 'POST':
        form = EstrategiaForm(request.POST, instance=estrategia)
        if form.is_valid():
            form.save()
            # Agregar mensaje de éxito
            messages.success(request, "Estrategia actualizada correctamente.")
            return redirect('estrategia_list')
        else:
            # Manejar errores de validación
            messages.error(request, "Hubo un error al actualizar la estrategia. Por favor revisa los datos ingresados.")
    else:
        form = EstrategiaForm(instance=estrategia)
    context = {'form': form, 'estrategia': estrategia}
    return render(request, 'formulario_estrategia.html', context)

def estrategia_delete(request, pk):
    estrategia = get_object_or_404(Estrategia, pk=pk)
    if request.method == 'POST':
        estrategia.delete()
        # Mensaje de éxito
        messages.success(request, "Estrategia eliminada correctamente.")
        return redirect('estrategia_list')
    context = {'estrategia': estrategia}
    return render(request, 'estrategia_confirm_delete.html', context)

# Eventos
def evento_list(request):
    eventos = Evento.objects.all()
    context = {'eventos': eventos}
    return render(request, 'eventos.html', context)

def evento_detail(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    context = {'evento': evento}
    return render(request, 'evento_detail.html', context)

def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento registrado correctamente.")
            return redirect('evento_list')
        else:
            messages.error(request, "Hubo un error al registrar el evento. Por favor revisa los datos ingresados.")
    else:
        form = EventoForm()
    context = {'form': form}
    return render(request, 'formulario_evento.html', context)

def evento_update(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento actualizado correctamente.")
            return redirect('evento_list')
        else:
            messages.error(request, "Hubo un error al actualizar el evento. Por favor revisa los datos ingresados.")
    else:
        form = EventoForm(instance=evento)
    context = {'form': form, 'evento': evento}
    return render(request, 'formulario_evento.html', context)

def evento_delete(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, "Evento eliminado correctamente.")
        return redirect('evento_list')
    context = {'evento': evento}
    return render(request, 'evento_confirm_delete.html', context)

#profesores
def profesor_list(request):
    profesores = Profesor.objects.all()
    context = {'profesores': profesores}
    return render(request, 'profesores.html', context)

def profesor_detail(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    context = {'profesor': profesor}
    return render(request, 'profesor_detail.html', context)

def profesor_create(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Profesor registrado correctamente.")
            return redirect('profesor_list')
        else:
            messages.error(request, "Hubo un error al registrar el profesor. Por favor revisa los datos ingresados.")
    else:
        form = ProfesorForm()
    context = {'form': form}
    return render(request, 'formulario_informacion_pro.html', context)

def profesor_update(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            messages.success(request, "Profesor actualizado correctamente.")
            return redirect('profesor_list')
        else:
            messages.error(request, "Hubo un error al actualizar el profesor. Por favor revisa los datos ingresados.")
    else:
        form = ProfesorForm(instance=profesor)
    context = {'form': form, 'profesor': profesor}
    return render(request, 'formulario_informacion_pro.html', context)

def profesor_delete(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
        messages.success(request, "Profesor eliminado correctamente.")
        return redirect('profesor_list')
    context = {'profesor': profesor}
    return render(request, 'profesor_confirm_delete.html', context)

#reporte
def reporte_list(request):
    reportes = Reporte.objects.all()
    context = {'reportes': reportes}
    return render(request, 'data_models/reporte_list.html', context)

def reporte_detail(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    context = {'reporte': reporte}
    return render(request, 'reporte_detail.html', context)

def reporte_create(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Reporte registrado correctamente.")
            return redirect('reporte_list')
        else:
            messages.error(request, "Hubo un error al registrar el reporte. Por favor revisa los datos ingresados.")
    else:
        form = ReporteForm()
    context = {'form': form}
    return render(request, 'formulario_reporte.html', context)

def reporte_update(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    if request.method == 'POST':
        form = ReporteForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            messages.success(request, "Reporte actualizado correctamente.")
            return redirect('reporte_list')
        else:
            messages.error(request, "Hubo un error al actualizar el reporte. Por favor revisa los datos ingresados.")
    else:
        form = ReporteForm(instance=reporte)
    context = {'form': form, 'reporte': reporte}
    return render(request, 'formulario_reporte.html', context)

def reporte_delete(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    if request.method == 'POST':
        reporte.delete()
        messages.success(request, "Reporte eliminado correctamente.")
        return redirect('reporte_list')
    context = {'reporte': reporte}
    return render(request, 'reporte_confirm_delete.html', context)

# Usuario
def registro_usuario_list(request):
    usuarios = RegistroUsuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'usuarios.html', context)

def registro_usuario_detail(request, pk):
    usuario = get_object_or_404(RegistroUsuario, pk=pk)
    context = {'usuario': usuario}
    return render(request, 'registro_usuario_detail.html', context)

def registro_usuario_create(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado correctamente.")
            return redirect('registro_usuario_list')
        else:
            messages.error(request, "Hubo un error al registrar el usuario. Por favor revisa los datos ingresados.")
    else:
        form = RegistroUsuarioForm()
    context = {'form': form}
    return render(request, 'formulario_usuario.html', context)

def registro_usuario_update(request, pk):
    usuario = get_object_or_404(RegistroUsuario, pk=pk)
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado correctamente.")
            return redirect('registro_usuario_list')
        else:
            messages.error(request, "Hubo un error al actualizar el usuario. Por favor revisa los datos ingresados.")
    else:
        form = RegistroUsuarioForm(instance=usuario)
    context = {'form': form, 'usuario': usuario}
    return render(request, 'formulario_usuario.html', context)

def registro_usuario_delete(request, pk):
    usuario = get_object_or_404(RegistroUsuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, "Usuario eliminado correctamente.")
        return redirect('registro_usuario_list')
    context = {'usuario': usuario}
    return render(request, 'registro_usuario_confirm_delete.html', context)

# Encuesta
def encuesta_list(request):
    encuestas = Encuesta.objects.all()
    context = {'encuestas': encuestas}
    return render(request, 'encuestas.html', context)

def encuesta_detail(request, pk):
    encuesta = get_object_or_404(Encuesta, pk=pk)
    context = {'encuesta': encuesta}
    return render(request, 'encuesta_detail.html', context)

def encuesta_create(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        autor = request.POST.get('autor')
        estado = request.POST.get('estado')

        if titulo and descripcion and autor and estado:
            # Crear la encuesta
            encuesta = Encuesta.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                autor=autor,
                estado=estado
            )

            # Crear las preguntas asociadas
            preguntas = request.POST.getlist('preguntas[]')
            for texto_pregunta in preguntas:
                if texto_pregunta.strip():  # Evitar preguntas vacías
                    Pregunta.objects.create(encuesta=encuesta, texto=texto_pregunta)

            messages.success(request, "Encuesta creada correctamente.")
            return redirect('encuesta_list')
        else:
            messages.error(request, "Todos los campos son obligatorios.")
    return render(request, 'formulario_encuesta.html')

def encuesta_update(request, pk):
    encuesta = get_object_or_404(Encuesta, pk=pk)
    if request.method == 'POST':
        form = EncuestaForm(request.POST, instance=encuesta)
        if form.is_valid():
            form.save()
            messages.success(request, "Encuesta actualizada correctamente.")
            return redirect('encuesta_list')
        else:
            messages.error(request, "Hubo un error al actualizar la encuesta. Por favor revisa los datos ingresados.")
    else:
        form = EncuestaForm(instance=encuesta)
    context = {'form': form, 'encuesta': encuesta}
    return render(request, 'formulario_encuesta.html', context)

def encuesta_delete(request, pk):
    encuesta = get_object_or_404(Encuesta, pk=pk)
    if request.method == 'POST':
        encuesta.delete()
        messages.success(request, "Encuesta eliminada correctamente.")
        return redirect('encuesta_list')
    context = {'encuesta': encuesta}
    return render(request, 'encuesta_confirm_delete.html', context)
