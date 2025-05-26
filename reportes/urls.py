from django.urls import path
from reportes.vistas import vistas_principal
from reportes.vistas import vistas_usuario

urlpatterns = [
    #----------------------------------------
    #REPORTES

    #Crear Reporte
    path('p/formular/reporte/', vistas_principal.crearReporte, name='p_formular_reporte'),
    #Ver multiples Reportes
    path('p/reportes/', vistas_principal.visualizarReportes, name='p_reportes'),
    #Ver una unica Reporte
    path('p/visualizar/reporte/<int:reporte_id>/', vistas_principal.visualizarReporte, name='p_visualizar_reporte'),
    #Modificar muliples Reportes
    path('p/modificar/reporte/<int:reporte_id>/', vistas_principal.modificarReporte, name='p_modificar_reporte'), 
    #Eliminar una unica Reporte
    path('p/eliminar/reporte/<int:reporte_id>/', vistas_principal.eliminarReporte, name='p_eliminar_reporte'),
    #Eliminar multiples Reportes
    path('p/eliminar/reportes/', vistas_principal.eliminarReportes, name='p_eliminar_reportes'),
    #Ver multiples Reportes
    path('reportes/', vistas_usuario.visualizarReportes, name='reportes'),
    #Ver una unica Reporte
    path('visualizar_reporte/<int:reporte_id>/', vistas_usuario.visualizarReporte, name='visualizar_reporte'),
    
    
]
