from django.urls import path
from encuestas.vistas import vistas_usuario
from encuestas.vistas import vistas_principal

urlpatterns = [
    #----------------------------------------
    #ENCUESTAS

    #Crear Encuesta
    path('principal_formular_encuesta/', vistas_principal.crearEncuesta, name='principal_formular_encuesta'),
    #Ver multiples Encuestas
    path('principal_encuestas/', vistas_principal.visualizarEncuestas, name='principal_encuestas'),
    #Ver una unica Encuesta
    path('principal_visualizar_encuesta/<int:encuesta_id>/', vistas_principal.visualizarEncuesta, name='principal_visualizar_encuesta'),
    #Modificar muliples Encuestas
    path('principal_modificar_encuesta/<int:encuesta_id>/', vistas_principal.modificarEncuesta, name='principal_modificar_encuesta'), 
    #Eliminar una unica Encuesta
    path('principal_eliminar_encuesta/<int:encuesta_id>/', vistas_principal.eliminarEncuesta, name='principal_eliminar_encuesta'),
    #Eliminar multiples Encuestas
    path('principal_eliminar_encuestas/', vistas_principal.eliminarEncuestas, name='principal_eliminar_encuestas'),
    # Nueva URL para realizar encuesta
    path('realizar_encuesta/<int:encuesta_id>/', vistas_usuario.realizar_encuesta, name='realizar_encuesta'),
    #Ver multiples Encuestas
    path('encuestas/', vistas_usuario.visualizarEncuestas, name='encuestas'),
    #Ver una unica Encuesta
    path('visualizar_encuesta/<int:encuesta_id>/', vistas_usuario.visualizarEncuesta, name='visualizar_encuesta'),
    
    #----------------------------------------
    
]
