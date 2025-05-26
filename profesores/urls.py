from django.urls import path
from profesores.vistas import vistas_principal
from profesores.vistas import vistas_usuario
urlpatterns = [
    #----------------------------------------
    #PROFESORES

    #Crear Profesor
    path('p/formular/profesor/', vistas_principal.crearProfesor, name='p_formular_profesor'),
    #Ver multiples Profesores
    path('p/profesores/', vistas_principal.visualizarProfesores, name='p_profesores'),

    #Ver una unica Profesor
    path('p/visualizar/profesor/<int:profesor_id>/', vistas_principal.visualizarProfesor, name='p_visualizar_profesor'),
    #Modificar muliples Profesores
    path('p/modificar/profesor/<int:profesor_id>/', vistas_principal.modificarProfesor, name='p_modificar_profesor'), 
    #Eliminar una unica Profesor
    path('p/eliminar/profesor/<int:profesor_id>/', vistas_principal.eliminarProfesor, name='p_eliminar_profesor'),
    #Eliminar multiples Profesores
    path('p/eliminar/profesores/', vistas_principal.eliminarProfesores, name='p_eliminar_profesores'),

    #Ver multiples Profesores
    path('profesores/', vistas_usuario.visualizarProfesores, name='profesores'),
    #Ver una unica Profesor
    path('visualizar/profesor/<int:profesor_id>/', vistas_usuario.visualizarProfesor, name='visualizar_profesor'),
    
    
]
