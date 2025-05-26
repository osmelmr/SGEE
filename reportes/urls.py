from django.urls import path
from reportes.vistas import vistas_principal
from reportes.vistas import vistas_usuario

urlpatterns = [
    #----------------------------------------
    #REPORTES

    #Crear Reporte
    path('principal_formular_reporte/', vistas_principal.crearReporte, name='principal_formular_reporte'),
    #Ver multiples Reportes
    path('principal_reportes/', vistas_principal.visualizarReportes, name='principal_reportes'),
    #Ver una unica Reporte
    path('principal_visualizar_reporte/<int:reporte_id>/', vistas_principal.visualizarReporte, name='principal_visualizar_reporte'),
    #Modificar muliples Reportes
    path('principal_modificar_reporte/<int:reporte_id>/', vistas_principal.modificarReporte, name='principal_modificar_reporte'), 
    #Eliminar una unica Reporte
    path('principal_eliminar_reporte/<int:reporte_id>/', vistas_principal.eliminarReporte, name='principal_eliminar_reporte'),
    #Eliminar multiples Reportes
    path('principal_eliminar_reportes/', vistas_principal.eliminarReportes, name='principal_eliminar_reportes'),
    #Ver multiples Reportes
    path('reportes/', vistas_usuario.visualizarReportes, name='reportes'),
    #Ver una unica Reporte
    path('visualizar_reporte/<int:reporte_id>/', vistas_usuario.visualizarReporte, name='visualizar_reporte'),
    
    
]
