from django.urls import path
from encuestas.vistas import vistas_usuario
from encuestas.vistas import vistas_principal

urlpatterns = [
    #----------------------------------------
    #ENCUESTAS

    #Crear Encuesta
    path('p/formular/encuesta/', vistas_principal.crear_encuesta, name='p_formular_encuesta'),
    #Ver multiples Encuestas
    path('p/encuestas/', vistas_principal.visualizar_encuestas, name='p_encuestas'),
    #Ver una unica Encuesta
    path('p/visualizar/encuesta/<int:encuesta_id>/', vistas_principal.visualizar_encuesta, name='p_visualizar_encuesta'),
    #Modificar muliples Encuestas
    path('p/modificar/encuesta/<int:encuesta_id>/', vistas_principal.modificar_encuesta, name='p_modificar_encuesta'), 
    #Eliminar una unica Encuesta
    path('p/eliminar/encuesta/<int:encuesta_id>/', vistas_principal.eliminar_encuesta, name='p_eliminar_encuesta'),
    #Eliminar multiples Encuestas
    path('p/eliminar/encuestas/', vistas_principal.eliminar_encuestas, name='p_eliminar_encuestas'),
    # Nueva URL para realizar encuesta
    path('realizar/encuesta/<int:encuesta_id>/', vistas_usuario.realizar_encuesta, name='realizar_encuesta'),
    #Ver multiples Encuestas
    path('encuestas/', vistas_usuario.visualizar_encuestas, name='encuestas'),
    #Ver una unica Encuesta
    path('visualizar/encuesta/<int:encuesta_id>/', vistas_usuario.visualizar_encuesta, name='visualizar_encuesta'),
    
    #----------------------------------------
    
]
