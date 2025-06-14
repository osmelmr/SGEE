from django.urls import path
from grupos.vistas import vistas_principal
from grupos.vistas import vistas_usuario

urlpatterns = [
    #----------------------------------------
    #GRUPOS URLS
    path('p/formular/grupo/', vistas_principal.crear_grupo, name='p_formular_grupo'),  
    path('p/grupos/', vistas_principal.listar_grupos, name='p_grupos'),
    path('p/visualizar/grupo/<int:grupo_id>/', vistas_principal.visualizar_grupo, name='p_visualizar_grupo'),
    path('p/modificar/grupo/<int:grupo_id>/', vistas_principal.modificar_grupo, name='p_modificar_grupo'),
    path('p/eliminar/grupo/<int:grupo_id>/', vistas_principal.eliminar_grupo, name='p_eliminar_grupo'),
    path('p/eliminar/grupos/', vistas_principal.eliminar_grupos, name='p_eliminar_grupos'),  # <-- Cambia aquí, elimina <int:grupo_id>

    path('grupos/', vistas_usuario.visualizar_grupos, name='grupos'),
    path('visualizar/grupo/<int:grupo_id>/', vistas_usuario.visualizar_grupo, name='visualizar_grupo'),

]
