from django.urls import path
from usuarios.vistas import vistas_principal
from usuarios.vistas import vistas_usuario

urlpatterns = [
    #USUARIOS

    #Crear Usuario
    path('p/formular/usuario/', vistas_principal.crearUsuario, name='p_formular_usuario'),
    #Ver multiples Usuarios
    path('p/usuarios/', vistas_principal.visualizarUsuarios, name='p_usuarios'),
    #Ver una unica Usuario
    path('p/visualizar/usuario/<int:usuario_id>/', vistas_principal.visualizarUsuario, name='p_visualizar_usuario'),
    #Modificar muliples Usuarios
    path('p/modificar/usuario/<int:usuario_id>/', vistas_principal.modificarUsuario, name='p_modificar_usuario'), 
    #Eliminar una unica Usuario
    path('p/eliminar/usuario/<int:usuario_id>/', vistas_principal.eliminarUsuario, name='p_eliminar_usuario'),
    #Eliminar multiples Usuarios
    path('p/eliminar/usuarios/', vistas_principal.eliminarUsuarios, name='p_eliminar_usuarios'),
    #Ver multiples Usuarios
    path('usuarios/', vistas_usuario.visualizarUsuarios, name='usuarios'),
    #Ver una unica Usuario
    path('visualizar/usuario/<int:usuario_id>/', vistas_usuario.visualizarUsuario, name='visualizar_usuario'),
    
]
