from django.urls import path
from reportes.vistas import vistas_principal
from reportes.vistas import vistas_usuario

urlpatterns = [
    #----------------------------------------
    #REPORTES

    #Crear Reporte
    path('p/formular/reporte/', vistas_principal.crear_reporte, name='p_formular_reporte'),
    #Ver multiples Reportes
    path('p/reportes/', vistas_principal.visualizar_reportes, name='p_reportes'),
    #Ver una unica Reporte
    path('p/visualizar/reporte/<int:reporte_id>/', vistas_principal.visualizar_reporte, name='p_visualizar_reporte'),
    #Modificar muliples Reportes
    path('p/modificar/reporte/<int:reporte_id>/', vistas_principal.modificar_reporte, name='p_modificar_reporte'), 
    #Eliminar una unica Reporte
    path('p/eliminar/reporte/<int:reporte_id>/', vistas_principal.eliminar_reporte, name='p_eliminar_reporte'),
    #Eliminar multiples Reportes
    path('p/eliminar/reportes/', vistas_principal.eliminar_reportes, name='p_eliminar_reportes'),
    #Ver multiples Reportes
    path('reportes/', vistas_usuario.visualizar_reportes, name='reportes'),
    #Ver una unica Reporte
    path('visualizar_reporte/<int:reporte_id>/', vistas_usuario.visualizar_reporte, name='visualizar_reporte'),
    
    
]
