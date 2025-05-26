from django.urls import path
from profesores.vistas import vistas_principal
from profesores.vistas import vistas_usuario
urlpatterns = [
    #----------------------------------------
    #PROFESORES

    #Crear Profesor
    path('principal_formular_profesor/', vistas_principal.crearProfesor, name='principal_formular_profesor'),
    #Ver multiples Profesores
    path('principal_profesores/', vistas_principal.visualizarProfesores, name='principal_profesores'),

    #Ver una unica Profesor
    path('principal_visualizar_profesor/<int:profesor_id>/', vistas_principal.visualizarProfesor, name='principal_visualizar_profesor'),
    #Modificar muliples Profesores
    path('principal_modificar_profesor/<int:profesor_id>/', vistas_principal.modificarProfesor, name='principal_modificar_profesor'), 
    #Eliminar una unica Profesor
    path('principal_eliminar_profesor/<int:profesor_id>/', vistas_principal.eliminarProfesor, name='principal_eliminar_profesor'),
    #Eliminar multiples Profesores
    path('principal_eliminar_profesores/', vistas_principal.eliminarProfesores, name='principal_eliminar_profesores'),
    
    
]
