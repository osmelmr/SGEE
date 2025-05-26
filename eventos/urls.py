from django.urls import path
from eventos.vistas import vistas_principal
from eventos.vistas import vistas_usuario

urlpatterns = [
    #----------------------------------------
    #EVENTOS

    #Crear Evento
    path('p/formular/evento/', vistas_principal.crearEvento, name='p_formular_evento'),
    #Ver multiples Eventos
    path('p/eventos/', vistas_principal.visualizarEventos, name='p_eventos'),
    #Ver una unica Evento
    path('p/visualizar/evento/<int:evento_id>/', vistas_principal.visualizarEvento, name='p_visualizar_evento'),
    #Modificar muliples Eventos
    path('p/modificar/evento/<int:evento_id>/', vistas_principal.modificarEvento, name='p_modificar_evento'), 
    #Eliminar una unica Evento
    path('p/eliminar/evento/<int:evento_id>/', vistas_principal.eliminarEvento, name='p_eliminar_evento'),
    #Eliminar multiples Eventos
    path('p/eliminar/eventos/', vistas_principal.eliminarEventos, name='p_eliminar_eventos'),
    #Inscribir en un evento
    path('inscribir/evento/<int:evento_id>/', vistas_usuario.toggleEvento, name='inscribir_evento'),
    #Ver multiples Eventos
    path('eventos/', vistas_usuario.visualizarEventos, name='eventos'),
    #Ver una unica Evento
    path('visualizar/evento/<int:evento_id>/', vistas_usuario.visualizarEvento, name='visualizar_evento'),
    
    
]
