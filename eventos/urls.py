from django.urls import path
from eventos.vistas import vistas_principal
from eventos.vistas import vistas_usuario

urlpatterns = [
    #----------------------------------------
    #EVENTOS

    #Crear Evento
    path('principal_formular_evento/', vistas_principal.crearEvento, name='principal_formular_evento'),
    #Ver multiples Eventos
    path('principal_eventos/', vistas_principal.visualizarEventos, name='principal_eventos'),
    #Ver una unica Evento
    path('principal_visualizar_evento/<int:evento_id>/', vistas_principal.visualizarEvento, name='principal_visualizar_evento'),
    #Modificar muliples Eventos
    path('principal_modificar_evento/<int:evento_id>/', vistas_principal.modificarEvento, name='principal_modificar_evento'), 
    #Eliminar una unica Evento
    path('principal_eliminar_evento/<int:evento_id>/', vistas_principal.eliminarEvento, name='principal_eliminar_evento'),
    #Eliminar multiples Eventos
    path('principal_eliminar_eventos/', vistas_principal.eliminarEventos, name='principal_eliminar_eventos'),
    #Inscribir en un evento
    path('inscribir_evento/<int:evento_id>/', vistas_usuario.toggleEvento, name='inscribir_evento'),
    #Ver multiples Eventos
    path('eventos/', vistas_usuario.visualizarEventos, name='eventos'),
    #Ver una unica Evento
    path('visualizar_evento/<int:evento_id>/', vistas_usuario.visualizarEvento, name='visualizar_evento'),
    
    
]
