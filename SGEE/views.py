from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from data_models.models import Estrategia, Evento, Profesor, Reporte, Encuesta
from data_models.forms import ProfesorForm
from django.http import JsonResponse

def estra_view(request):
    return render(request, 'estra.html')

def contact_view(request):
    return render(request, 'contactenos.html')

def estrategias_view(request):
    estrat=Estrategia.objects.all()
    return render(request, 'estrategias.html',{'estrategias':estrat})

def eventos_view(request):
    # Obtener todos los eventos de la base de datos
    eventos = Evento.objects.all()
    # Pasar los eventos al contexto de la plantilla
    return render(request, 'eventos.html', {'eventos': eventos})

def reportes_view(request):
    reportes = Reporte.objects.all()
    return render(request, 'reportes.html', {'reportes': reportes})
                  
def usuarios_view(request):
    return render(request, 'usuarios.html')

def informacion_profesoral_view(request):
    profesores = Profesor.objects.all()
    # Pasar los profesores al contexto de la plantilla          
    return render(request, 'informacion_profesoral.html', {'profesores': profesores})

def encuestas_view(request):
    encuestas = Encuesta.objects.all()
    return render(request, 'encuestas.html', {'encuestas': encuestas})

def sobrenos_view(request):
    return render(request, 'sobrenos.html')

def testimonials_view(request):
    return render(request, 'testimonials.html')

def formulario_encuesta_view(request):
    return render(request, 'formulario_encuesta.html')

def formulario_estrategia_view(request):
    if request.method == 'POST':
        # Recopilar datos del formulario utilizando los nombres originales
        titulo_estrategia = request.POST.get('titulo-estrategia')  # Nombre en el formulario
        curso = request.POST.get('curso')  # Curso
        anio_escolar = request.POST.get('ano-escolar')  # Año escolar
        grupo = request.POST.get('grupo')  # Grupo

        plan_estudios = request.POST.get('plan-estudios')  # Plan de estudios
        obj_estrategia = request.POST.get('objetivos-estrategia')  # Objetivos de la estrategia
        dir_brigada = request.POST.get('direccion-brigada')  # Dirección de la brigada
        caract_brigada = request.POST.get('caracteristicas-brigada')  # Características de la brigada
        colect_pedagogico = request.POST.get('colectivo-pedagogico')  # Colectivo pedagógico
        otros_aspectos = request.POST.get('otros-aspectos', 'otros_aspectos')  # Otros aspectos (valor por defecto)

        dim_curricular = request.POST.get('dimension-curricular')  # Dimensión curricular
        dim_extensionista = request.POST.get('dimension-extensionista')  # Dimensión extensionista
        dim_politica = request.POST.get('dimension-politico-ideologica')  # Dimensión político-ideológica
        conclusiones = request.POST.get('conclusiones')  # Conclusiones

        obj_general = request.POST.get('objetivo-general')  # Objetivo general
        obj_dc = request.POST.get('objetivos-especificos-curricular')  # Objetivos específicos (curricular)
        plan_dc = request.POST.get('plan-acciones-curricular')  # Plan de acciones (curricular)
        obj_de = request.POST.get('objetivos-especificos-extensionista')  # Objetivos específicos (extensionista)
        plan_de = request.POST.get('plan-acciones-extensionista')  # Plan de acciones (extensionista)
        obj_dp = request.POST.get('objetivos-especificos-politico-ideologica')  # Objetivos específicos (político-ideológica)
        plan_dp = request.POST.get('plan-acciones-politico-ideologica')  # Plan de acciones (político-ideológica)

        evaluacion = request.POST.get('evaluacion-integral')  # Evaluación integral
        autor = request.POST.get('autor')  # Nombre del autor

        # Crear una instancia del modelo Estrategia
        estrategia = Estrategia(
            nombre=titulo_estrategia,  # Mapeo con el modelo
            curso=curso,
            anio_escolar=anio_escolar,
            grupo=grupo,
            plan_estudios=plan_estudios,
            obj_estrategia=obj_estrategia,
            dir_brigada=dir_brigada,
            caract_brigada=caract_brigada,
            colect_pedagogico=colect_pedagogico,
            otros_aspectos=otros_aspectos,
            dim_curricular=dim_curricular,
            dim_extensionista=dim_extensionista,
            dim_politica=dim_politica,
            conclusiones=conclusiones,
            obj_general=obj_general,
            obj_dc=obj_dc,
            plan_dc=plan_dc,
            obj_de=obj_de,
            plan_de=plan_de,
            obj_dp=obj_dp,
            plan_dp=plan_dp,
            evaluacion=evaluacion,
            autor=autor,
        )

        # Guardar la estrategia en la base de datos
        estrategia.save()

        # Redirigir a una página de éxito
        return redirect('estrategias')  # Cambia 'success_page' por la URL de tu página de éxito

    # Renderizar el formulario en caso de que el método sea GET
    return render(request, 'formulario_estrategia.html')

def formulario_evento_view(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre_evento = request.POST.get('nombre-evento')
        fecha_inicio = request.POST.get('fecha-inicio')
        fecha_fin = request.POST.get('fecha-fin')
        hora_inicio = request.POST.get('hora-inicio')
        hora_fin = request.POST.get('hora-fin')
        ubicacion_evento = request.POST.get('ubicacion-evento')
        tipo_evento = request.POST.get('tipo-evento')
        descripcion_evento = request.POST.get('descripcion-evento')
        profesor_cargo = request.POST.get('profesor-cargo')
        telefono_contacto = request.POST.get('telefono-contacto')

        # Validar campos obligatorios
        if not (nombre_evento and fecha_inicio and fecha_fin and hora_inicio and hora_fin and ubicacion_evento and tipo_evento and descripcion_evento and profesor_cargo and telefono_contacto):
            messages.error(request, "Todos los campos obligatorios deben ser completados.")
            return render(request, 'formulario_evento.html')

        # Crear y guardar el evento
        evento = Evento(
            nombre_evento=nombre_evento,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            ubicacion_evento=ubicacion_evento,
            tipo_evento=tipo_evento,
            descripcion=descripcion_evento,
            profesor_cargo=profesor_cargo,
            telefono_contacto=telefono_contacto
        )
        try:
            evento.save()
            messages.success(request, "Evento registrado correctamente.")
            return redirect('eventos')  # Redirigir a la lista de eventos
        except Exception as e:
            messages.error(request, f"Hubo un error al registrar el evento: {str(e)}")
            return render(request, 'formulario_evento.html')

    # Renderizar el formulario en caso de GET
    return render(request, 'formulario_evento.html')

def formulario_usuario_view(request):
    return render(request, 'formulario_usuario.html')

def formulario_reporte_view(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        brigada = request.POST.get('brigada')
        codigo = request.POST.get('codigo')
        periodo = request.POST.get('periodo')
        fecha = request.POST.get('fecha')
        autor = request.POST.get('autor')
        institucion = request.POST.get('institucion')
        resumen = request.POST.get('resumen')
        objetivos = request.POST.get('objetivos')
        actividades = request.POST.get('actividades')
        resultados = request.POST.get('resultados')
        analisis = request.POST.get('analisis')
        desafios = request.POST.get('desafios')
        proximos_pasos = request.POST.get('proximos-pasos')
        anexos = request.FILES.get('anexos')  # Manejo de archivos
        print("llega")

        # Crear y guardar el reporte
        reporte = Reporte(
            brigada=brigada,
            codigo=codigo,
            periodo=periodo,
            fecha=fecha,
            autor=autor,
            institucion=institucion,
            resumen=resumen,
            objetivos=objetivos,
            actividades=actividades,
            resultados=resultados,
            analisis=analisis,
            desafios=desafios,
            proximos_pasos=proximos_pasos,
            anexos=anexos
        )
        try:
            reporte.save()
            messages.success(request, "Reporte registrado correctamente.")
            return redirect('reportes')  # Redirigir a la lista de reportes
        except Exception as e:
            messages.error(request, f"Hubo un error al registrar el reporte: {str(e)}")
            return render(request, 'formulario_reporte.html')

    # Renderizar el formulario en caso de GET
    return render(request, 'formulario_reporte.html')

def formulario_informacion_pro_view(request):
    if request.method == 'POST':
        # Recopilar datos del formulario
        nombre = request.POST.get('nombre-profesor')
        primer_apellido = request.POST.get('primer-apellido')
        segundo_apellido = request.POST.get('segundo-apellido')
        sexo = request.POST.get('sexo')
        categoria_docente = request.POST.get('categoria-docente')
        asignatura = request.POST.get('asignatura')
        solapin = request.POST.get('solapin')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        brigada_asignada = request.POST.get('brigada-asignada')
        brigadas_impartir = request.POST.get('brigadas-impartir')
        descripcion = request.POST.get('descripcion-profesor')

        # Validar campos obligatorios
        if not nombre or not primer_apellido or not sexo or not categoria_docente or not asignatura or not solapin or not telefono or not correo or not brigada_asignada or not brigadas_impartir or not descripcion:
            messages.error(request, "Todos los campos obligatorios deben ser completados.")
            return render(request, 'formulario_informacion_pro.html')

        # Crear una instancia del modelo Profesor
        profesor = Profesor(
            nombre=nombre,
            primer_apellido=primer_apellido,
            segundo_apellido=segundo_apellido,
            sexo=sexo,
            categoria_docente=categoria_docente,
            asignatura=asignatura,
            solapin=solapin,
            telefono=telefono,
            correo=correo,
            brigada_asignada=brigada_asignada,
            brigadas_impartir=brigadas_impartir,
            descripcion=descripcion
        )

        # Guardar el profesor en la base de datos
        try:
            profesor.save()
            messages.success(request, "Profesor registrado correctamente.")
            return redirect('informacion_profesoral')
        except Exception as e:
            messages.error(request, f"Hubo un error al registrar el profesor: {str(e)}")
            return render(request, 'formulario_informacion_pro.html')

    # Renderizar el formulario en caso de GET
    return render(request, 'formulario_informacion_pro.html')

def eliminarEstrategia(request, estra_id):
    estra=get_object_or_404(Estrategia, id=estra_id)
    estra.delete()
    return redirect('estrategias')

def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    messages.success(request, "Evento eliminado correctamente.")
    return redirect('eventos')

def eliminar_reporte(request, reporte_id):
    reporte = get_object_or_404(Reporte, id=reporte_id)
    reporte.delete()
    messages.success(request, "reporte eliminado correctamente.")
    return redirect('reportes')

def eliminar_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    profesor.delete()
    messages.success(request, "Profesor eliminado correctamente.")
    return redirect('informacion_profesoral')

def eliminar_encuesta(request, encuesta_id):
    encuesta = get_object_or_404(Encuesta, id=encuesta_id)
    encuesta.delete()
    messages.success(request, "encuesta eliminada correctamente.")
    return redirect('encuestas')

def eliminar_estrategias(request):
    if request.method == 'POST':
        # Obtener los IDs de las estrategias seleccionadas
        estrategias_ids = request.POST.getlist('estrategias[]')
        if estrategias_ids:
            # Eliminar las estrategias seleccionadas
            Estrategia.objects.filter(id__in=estrategias_ids).delete()
            messages.success(request, "Estrategias eliminadas correctamente.")
        else:
            messages.error(request, "No se seleccionaron estrategias para eliminar.")
        return redirect('estrategias')
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def eliminar_eventos(request):
    if request.method == 'POST':
        # Obtener los IDs de los eventos seleccionados
        eventos_ids = request.POST.getlist('eventos[]')
        if eventos_ids:
            # Eliminar los eventos seleccionados
            Evento.objects.filter(id__in=eventos_ids).delete()
            messages.success(request, "Eventos eliminados correctamente.")
        else:
            messages.error(request, "No se seleccionaron eventos para eliminar.")
        return redirect('eventos')
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def eliminar_profesores(request):
    if request.method == 'POST':
        # Obtener los IDs de los profesores seleccionados
        profesores_ids = request.POST.getlist('profesores[]')
        if profesores_ids:
            # Eliminar los profesores seleccionados
            Profesor.objects.filter(id__in=profesores_ids).delete()
            messages.success(request, "Profesores eliminados correctamente.")
        else:
            messages.error(request, "No se seleccionaron profesores para eliminar.")
        return redirect('informacion_profesoral')
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def eliminar_encuestas(request):
    if request.method == 'POST':
        encuestas_ids = request.POST.getlist('encuestas[]')
        if encuestas_ids:
            Encuesta.objects.filter(id__in=encuestas_ids).delete()
            messages.success(request, "Encuestas eliminadas correctamente.")
        else:
            messages.error(request, "No se seleccionaron encuestas para eliminar.")
        return redirect('encuestas')
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def eliminar_reportes(request):
    if request.method == 'POST':
        reportes_ids = request.POST.getlist('reportes[]')
        if reportes_ids:
            Reporte.objects.filter(id__in=reportes_ids).delete()
            messages.success(request, "Reportes eliminados correctamente.")
        else:
            messages.error(request, "No se seleccionaron reportes para eliminar.")
        return redirect('reportes')
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def eliminar_usuarios(request):
    if request.method == 'POST':
        usuarios_ids = request.POST.getlist('usuarios[]')
        if usuarios_ids:
            Usuario.objects.filter(id__in=usuarios_ids).delete()
            messages.success(request, "Usuarios eliminados correctamente.")
        else:
            messages.error(request, "No se seleccionaron usuarios para eliminar.")
        return redirect('usuarios')
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)