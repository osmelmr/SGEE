from django.urls import path
from estrategias.vistas import vistas_principal 
from estrategias.vistas import vistas_usuario
from estrategias.vistas import vistas_generales

urlpatterns = [
    #----------------------------------------
    #STRATEGYS

    #Create Strategy
    path('p/formular/estrategia/', vistas_principal.crearEstrategia, name='p_formular_estrategia'),
    #View Multiple Estrategys
    path('p/estrategias/', vistas_principal.visualizarEstrategias, name='p_estrategias'),
    #View Unique Estrategy
    path('p/visualizar/estrategia/<int:estra_id>/', vistas_principal.visualizarEstrategia, name='p_visualizar_estrategia'),
    #Update Unique Estrategy
    path('p/modificar/estrategia/<int:estra_id>/', vistas_principal.modificarEstrategia, name='p_modificar_estrategia'), 
    #Delete Unique Estrategy
    path('p/eliminar/estrategia/<int:estra_id>/', vistas_principal.eliminarEstrategia, name='p_eliminar_estrategia'),
    #Delete Multiple Estrategys
    path('p/eliminar/estrategias/', vistas_principal.eliminarEstrategias, name='p_eliminar_estrategias'),
    #Descargar estrategia pdf
    path('descargar/estrategia/pdf/<int:estra_id>/', vistas_generales.estrategia_pdf, name='descargar_estrategia_pdf'),
     #View Multiple Estrategys
    path('estrategias/', vistas_usuario.visualizarEstrategias, name='estrategias'),
    #View Unique Estrategy
    path('visualizar/estrategia/<int:estra_id>/', vistas_usuario.visualizarEstrategia, name='visualizar_estrategia'),

]
