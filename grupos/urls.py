from django.urls import path
from grupos.vistas import vistas_principal
from grupos.vistas import vistas_usuario

urlpatterns = [
    #----------------------------------------
    #GRUPOS URLS
    path('principal_formular_grupo/', vistas_principal.crearGrupo, name='principal_formular_grupo'),  
    path('principal_grupos/', vistas_principal.listarGrupos, name='principal_grupos'),
    path('principal_visiualizar_grupo/<int:grupo_id>/', vistas_principal.visualizarGrupo, name='principal_visualizar_grupo'),
    path('principal_modificar/grupo/<int:grupo_id>/', vistas_principal.modificarGrupo, name='principal_modificar_grupo'),
    path('principal_eliminar/<int:grupo_id>/', vistas_principal.eliminarGrupo, name='principal_eliminar_grupo'),
    path('principal_eliminar_grupos/<int:grupo_id>/', vistas_principal.eliminarGrupos, name='principal_eliminar_grupos'),

]
