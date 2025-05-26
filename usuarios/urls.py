from django.urls import path
from usuarios.vistas import vistas_principal
from usuarios.vistas import vistas_usuario

urlpatterns = [
    #USUARIOS

    #Crear Usuario
    path('p/formular/usuario/', vistas_principal.crear_usuario, name='p_formular_usuario'),
    #Ver multiples Usuarios
    path('p/usuarios/', vistas_principal.visualizar_usuarios, name='p_usuarios'),
    #Ver una unica Usuario
    path('p/visualizar/usuario/<int:usuario_id>/', vistas_principal.visualizar_usuario, name='p_visualizar_usuario'),
    #Modificar muliples Usuarios
    path('p/modificar/usuario/<int:usuario_id>/', vistas_principal.modificar_usuario, name='p_modificar_usuario'), 
    #Eliminar una unica Usuario
    path('p/eliminar/usuario/<int:usuario_id>/', vistas_principal.eliminar_usuario, name='p_eliminar_usuario'),
    #Eliminar multiples Usuarios
    path('p/eliminar/usuarios/', vistas_principal.eliminar_usuarios, name='p_eliminar_usuarios'),
    #Ver multiples Usuarios
    path('usuarios/', vistas_usuario.visualizar_usuarios, name='usuarios'),
    #Ver una unica Usuario
    path('visualizar/usuario/<int:usuario_id>/', vistas_usuario.visualizar_usuario, name='visualizar_usuario'),
    
]
