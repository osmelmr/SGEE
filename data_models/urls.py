from django.urls import path
from data_models.vistas.vistasEstrategia.views import visualizarEstrategia, eliminarEstrategias,eliminarEstrategia,modificarEstrategia,visualizarEstrategias,crearEstrategia
from data_models.vistas.vistasEvento.views import visualizarEvento, eliminarEventos,eliminarEvento,modificarEvento,visualizarEventos,crearEvento
from data_models.vistas.vistasProfesor.views import visualizarProfesor, eliminarProfesores,eliminarProfesor,modificarProfesor,visualizarProfesores,crearProfesor
from data_models.vistas.vistasReporte.views import visualizarReporte, eliminarReportes,eliminarReporte,modificarReporte,visualizarReportes,crearReporte
from data_models.vistas.vistasEncuesta.views import visualizarEncuesta, eliminarEncuestas,eliminarEncuesta,modificarEncuesta,visualizarEncuestas,crearEncuesta
from data_models.vistas.vistasUsuario.views import visualizarUsuario, eliminarUsuarios,eliminarUsuario,modificarUsuario,visualizarUsuarios,crearUsuario
from data_models.vistas.vistasRolUsuario.views import visualizarEstrategiasG, principalG, visualizarEstrategiaG, visualizarProfesoresG, visualizarProfesorG, visualizarEventosG, visualizarEventoG, visualizarReportesG, visualizarReporteG, visualizarEncuestasG, visualizarEncuestaG, contact_view, sobrenos_view, visualizarTestimonios
from data_models.vistas.vistasGrupo.views import crearGrupo, listarGrupos, visualizarGrupo

urlpatterns = [
    #----------------------------------------
    #STRATEGYS

    #Create Strategy
    path('formular_estrategia/', crearEstrategia, name='formular_estrategia'),
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
    path('formular_evento/', crearEvento, name='formular_evento'),
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
    path('formular_profesor/', crearProfesor, name='formular_profesor'),
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
    path('formular_reporte/', crearReporte, name='formular_reporte'),
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
    path('formular_encuesta/', crearEncuesta, name='formular_encuesta'),
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
    path('formular_usuario/', crearUsuario, name='formular_usuario'),
    #Ver multiples Usuarios
    path('usuarios/', visualizarUsuarios, name='usuarios'),
    #Ver una unica Usuario
    path('visualizar_usuario/<int:usuario_id>/', visualizarUsuario, name='visualizar_usuario'),
    #Modificar muliples Usuarios
    path('modificar_usuario/<int:usuario_id>/', modificarUsuario, name='modificar_usuario'), 
    #Eliminar una unica Usuario
    path('eliminar_usuario/<int:usuario_id>/', eliminarUsuario, name='eliminar_usuario'),
    #Eliminar multiples Usuarios
    path('eliminar_usuarios/', eliminarUsuarios, name='eliminar_usuarios'),
    
    #----------------------------------------
    #GRUPOS URLS
    path('formular_grupo/', crearGrupo, name='formular_grupo'),  
    path('grupos/', listarGrupos, name='grupos'),
    path('grupos/<int:grupo_id>/', visualizarGrupo, name='visualizar_grupo'),

    #----------------------------------------
    #ESTUDIANTES URLS
    #View Multiple Estrategys
    path('pagina_principal_g/', principalG, name='pagina_principal_g'),
    path('estrategias_g/', visualizarEstrategiasG, name='estrategias_g'),
     #View Unique Estrategy
     path('visualizar_estrategia_g/<int:estra_id>/', visualizarEstrategiaG, name='visualizar_estrategia_g'),

     #Ver multiples Profesores
     path('profesores_g/', visualizarProfesoresG, name='profesores_g'),
     #Ver una unica Profesor
     path('visualizar_profesor_g/<int:profesor_id>/', visualizarProfesorG, name='visualizar_profesor_g'),
     #Ver multiples Eventos
     path('eventos_g/', visualizarEventosG, name='eventos_g'),
     #Ver una unica Evento
     path('visualizar_evento_g/<int:evento_id>/', visualizarEventoG, name='visualizar_evento_g'),

     #Ver multiples Reportes
     path('reportes_g/', visualizarReportesG, name='reportes_g'),
     #Ver una unica Reporte
     path('visualizar_reporte_g/<int:reporte_id>/', visualizarReporteG, name='visualizar_reporte_g'),

     #Ver multiples Encuestas
     path('encuestas_g/', visualizarEncuestasG, name='encuestas_g'),
     #Ver una unica Encuesta
     path('visualizar_encuesta_g/<int:encuesta_id>/', visualizarEncuestaG, name='visualizar_encuesta_g'),
     path('contactenos_g/',contact_view,name='contactar_g'),

     path('sobrenos_g/',sobrenos_view, name='sobrenos_g'),

     path('testimonials_g/',visualizarTestimonios, name='testimonials_g'),
     #----------------------------------------
]
