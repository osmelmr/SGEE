from django.urls import path
from eventos.vistas import vistas_principal
from eventos.vistas import vistas_usuario

urlpatterns = [
    #----------------------------------------
    #EVENTOS

    #Crear Evento
    path('p/formular/evento/', vistas_principal.crear_evento, name='p_formular_evento'),
    #Ver multiples Eventos
    path('p/eventos/', vistas_principal.visualizar_eventos, name='p_eventos'),
    #Ver una unica Evento
    path('p/visualizar/evento/<int:evento_id>/', vistas_principal.visualizar_evento, name='p_visualizar_evento'),
    #Modificar muliples Eventos
    path('p/modificar/evento/<int:evento_id>/', vistas_principal.modificar_evento, name='p_modificar_evento'), 
    #Eliminar una unica Evento
    path('p/eliminar/evento/<int:evento_id>/', vistas_principal.eliminar_evento, name='p_eliminar_evento'),
    #Eliminar multiples Eventos
    path('p/eliminar/eventos/', vistas_principal.eliminar_eventos, name='p_eliminar_eventos'),
    #Inscribir en un evento
    path('inscribir/evento/<int:evento_id>/', vistas_usuario.toggleEvento, name='inscribir_evento'),
    #Ver multiples Eventos
    path('eventos/', vistas_usuario.visualizar_eventos, name='eventos'),
    #Ver una unica Evento
    path('visualizar/evento/<int:evento_id>/', vistas_usuario.visualizar_evento, name='visualizar_evento'),
    
    
]
