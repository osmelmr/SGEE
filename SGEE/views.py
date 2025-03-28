from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from data_models.models import Estrategia, Evento, Profesor
from data_models.forms import ProfesorForm

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
    return render(request, 'reportes.html')

def usuarios_view(request):
    return render(request, 'usuarios.html')

def informacion_profesoral_view(request):
    profesores = Profesor.objects.all()
    # Pasar los profesores al contexto de la plantilla          
    return render(request, 'informacion_profesoral.html', {'profesores': profesores})

def encuestas_view(request):
    return render(request, 'encuestas.html')

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
        estrategia_id = request.POST.get('estrategia')  # ID de la estrategia seleccionada
        estrategia = get_object_or_404(Estrategia, id=estrategia_id)

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

        # Crear y guardar el objeto Evento
        evento = Evento(
            estrategia=estrategia,
            nombre_evento=nombre_evento,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            ubicacion_evento=ubicacion_evento,
            tipo_evento=tipo_evento,
            descripcion_evento=descripcion_evento,
            profesor_cargo=profesor_cargo,
            telefono_contacto=telefono_contacto
        )
        evento.save()

        # Redirigir a la página de eventos
        return redirect('eventos')

    # Renderizar el formulario en caso de GET
    estrategias = Estrategia.objects.all()  # Obtener todas las estrategias para el dropdown
    return render(request, 'formulario_evento.html', {'estrategias': estrategias})

def formulario_usuario_view(request):
    return render(request, 'formulario_usuario.html')

def formulario_reporte_view(request):
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

def eliminar_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    profesor.delete()
    messages.success(request, "Profesor eliminado correctamente.")
    return redirect('informacion_profesoral')