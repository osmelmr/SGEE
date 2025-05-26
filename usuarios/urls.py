from django.urls import path
from usuarios.vistas import vistas_principal
from usuarios.vistas import vistas_usuario

urlpatterns = [
    #USUARIOS

    #Crear Usuario
    path('principal_formular_usuario/', vistas_principal.crearUsuario, name='principal_formular_usuario'),
    #Ver multiples Usuarios
    path('principal_usuarios/', vistas_principal.visualizarUsuarios, name='principal_usuarios'),
    #Ver una unica Usuario
    path('principal_visualizar_usuario/<int:usuario_id>/', vistas_principal.visualizarUsuario, name='principal_visualizar_usuario'),
    #Modificar muliples Usuarios
    path('principal_modificar_usuario/<int:usuario_id>/', vistas_principal.modificarUsuario, name='principal_modificar_usuario'), 
    #Eliminar una unica Usuario
    path('principal_eliminar_usuario/<int:usuario_id>/', vistas_principal.eliminarUsuario, name='principal_eliminar_usuario'),
    #Eliminar multiples Usuarios
    path('principal_eliminar_usuarios/', vistas_principal.eliminarUsuarios, name='principal_eliminar_usuarios'),
    #Ver multiples Usuarios
    path('usuarios/', vistas_usuario.visualizarUsuarios, name='usuarios'),
    #Ver una unica Usuario
    path('visualizar_usuario/<int:usuario_id>/', vistas_usuario.visualizarUsuario, name='visualizar_usuario'),
    
]
