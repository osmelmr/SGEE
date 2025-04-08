from django.urls import path
from data_models.vistas.vistasEstrategia.views import visualizarEstrategia, eliminarEstrategias,eliminarEstrategia,modificarEstrategia,visualizarEstrategias,crearEstrategia
from data_models.vistas.vistasEvento.views import visualizarEvento, eliminarEventos,eliminarEvento,modificarEvento,visualizarEventos,crearEvento
from data_models.vistas.vistasProfesor.views import visualizarProfesor, eliminarProfesores,eliminarProfesor,modificarProfesor,visualizarProfesores,crearProfesor
from data_models.vistas.vistasReporte.views import visualizarReporte, eliminarReportes,eliminarReporte,modificarReporte,visualizarReportes,crearReporte
from data_models.vistas.vistasEncuesta.views import visualizarEncuesta, eliminarEncuestas,eliminarEncuesta,modificarEncuesta,visualizarEncuestas,crearEncuesta
from data_models.vistas.vistasUsuario.views import visualizarUsuario, eliminarUsuarios,eliminarUsuario,modificarUsuario,visualizarUsuarios,crearUsuario


urlpatterns = [
    #----------------------------------------
    #STRATEGYS

    #Create Strategy
    path('formulario_estrategia/', crearEstrategia, name='formulario_estrategia'),
    #View Multiple Estrategys
    path('estrategias/', visualizarEstrategias, name='estrategias'),
    #View Unique Estrategy
    path('visualizar_estrategia/<int:estra_id>/', visualizarEstrategia, name='visualizar_estrategia'),
    #Update Unique Estrategy
    path('modificar_estrategia/<int:estra_id>/', modificarEstrategia, name='modificar_estrategia'), 
    #Delete Unique Estrategy
    path('eliminar_estrategia/<int:estra_id>/', eliminarEstrategia, name='eliminar_estrategia'),
    #Delete Multiple Estrategys
    path('eliminar_estrategias/', eliminarEstrategias, name='eliminar_estrategias'),
    
    #----------------------------------------
    #EVENTOS

    #Crear Evento
    path('formulario_evento/', crearEvento, name='formulario_evento'),
    #Ver multiples Eventos
    path('eventos/', visualizarEventos, name='eventos'),
    #Ver una unica Evento
    path('visualizar_evento/<int:evento_id>/', visualizarEvento, name='visualizar_evento'),
    #Modificar muliples Eventos
    path('modificar_evento/<int:evento_id>/', modificarEvento, name='modificar_evento'), 
    #Eliminar una unica Evento
    path('eliminar_evento/<int:evento_id>/', eliminarEvento, name='eliminar_evento'),
    #Eliminar multiples Eventos
    path('eliminar_eventos/', eliminarEventos, name='eliminar_eventos'),
    
    #----------------------------------------
    #PROFESORES

    #Crear Profesor
    path('formulario_profesor/', crearProfesor, name='formulario_profesor'),
    #Ver multiples Profesores
    path('profesores/', visualizarProfesores, name='profesores'),
    #Ver una unica Profesor
    path('visualizar_profesor/<int:profesor_id>/', visualizarProfesor, name='visualizar_profesor'),
    #Modificar muliples Profesores
    path('modificar_profesor/<int:profesor_id>/', modificarProfesor, name='modificar_profesor'), 
    #Eliminar una unica Profesor
    path('eliminar_profesor/<int:profesor_id>/', eliminarProfesor, name='eliminar_profesor'),
    #Eliminar multiples Profesores
    path('eliminar_profesores/', eliminarProfesores, name='eliminar_profesores'),
    
    #----------------------------------------
    #REPORTES

    #Crear Reporte
    path('formulario_reporte/', crearReporte, name='formulario_reporte'),
    #Ver multiples Reportes
    path('reportes/', visualizarReportes, name='reportes'),
    #Ver una unica Reporte
    path('visualizar_reporte/<int:reporte_id>/', visualizarReporte, name='visualizar_reporte'),
    #Modificar muliples Reportes
    path('modificar_reporte/<int:reporte_id>/', modificarReporte, name='modificar_reporte'), 
    #Eliminar una unica Reporte
    path('eliminar_reporte/<int:reporte_id>/', eliminarReporte, name='eliminar_reporte'),
    #Eliminar multiples Reportes
    path('eliminar_reportes/', eliminarReportes, name='eliminar_reportes'),
    
    #----------------------------------------
    #ENCUESTAS

    #Crear Encuesta
    path('formulario_encuesta/', crearEncuesta, name='formulario_encuesta'),
    #Ver multiples Encuestas
    path('encuestas/', visualizarEncuestas, name='encuestas'),
    #Ver una unica Encuesta
    path('visualizar_encuesta/<int:encuesta_id>/', visualizarEncuesta, name='visualizar_encuesta'),
    #Modificar muliples Encuestas
    path('modificar_encuesta/<int:encuesta_id>/', modificarEncuesta, name='modificar_encuesta'), 
    #Eliminar una unica Encuesta
    path('eliminar_encuesta/<int:encuesta_id>/', eliminarEncuesta, name='eliminar_encuesta'),
    #Eliminar multiples Encuestas
    path('eliminar_encuestas/', eliminarEncuestas, name='eliminar_encuestas'),
    
    #----------------------------------------
    #USUARIOS

    #Crear Usuario
    path('formulario_usuario/', crearUsuario, name='formulario_usuario'),
    #Ver multiples Usuarios
    path('usuarios/', visualizarUsuarios, name='usuarios'),
    #Ver una unica Usuario
    # path('visualizar_usuario/<int:usuario_id>/', visualizarUsuario, name='visualizar_usuario'),
    # #Modificar muliples Usuarios
    # path('modificar_usuario/<int:usuario_id>/', modificarUsuario, name='modificar_usuario'), 
    # #Eliminar una unica Usuario
    # path('eliminar_usuario/<int:usuario_id>/', eliminarUsuario, name='eliminar_usuario'),
    #Eliminar multiples Usuarios
    path('eliminar_usuarios/', eliminarUsuarios, name='eliminar_usuarios'),
    
    #----------------------------------------
]
