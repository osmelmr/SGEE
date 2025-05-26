from django.urls import path
from grupos.vistas import vistas_principal
from grupos.vistas import vistas_usuario

urlpatterns = [
    #----------------------------------------
    #GRUPOS URLS
    path('p/formular/grupo/', vistas_principal.crearGrupo, name='p_formular_grupo'),  
    path('p/grupos/', vistas_principal.listarGrupos, name='p_grupos'),
    path('p/visualizar/grupo/<int:grupo_id>/', vistas_principal.visualizarGrupo, name='p_visualizar_grupo'),
    path('p/modificar/grupo/<int:grupo_id>/', vistas_principal.modificarGrupo, name='p_modificar_grupo'),
    path('p/eliminar/<int:grupo_id>/', vistas_principal.eliminarGrupo, name='p_eliminar_grupo'),
    path('p/eliminar/grupos/<int:grupo_id>/', vistas_principal.eliminarGrupos, name='p_eliminar_grupos'),

    path('grupos/', vistas_usuario.listarGrupos, name='grupos'),
    path('visualizar/grupo/<int:grupo_id>/', vistas_usuario.visualizarGrupo, name='visualizar_grupo'),

]
