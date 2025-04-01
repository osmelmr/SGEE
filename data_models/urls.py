from django.urls import path
from . import views

urlpatterns = [
    # Rutas para el modelo Estrategia
    path('estrategia/', views.estrategia_list, name='estrategia_list'),
    path('estrategia/<int:pk>/', views.estrategia_detail, name='estrategia_detail'),
    path('estrategia/create/', views.estrategia_create, name='estrategia_create'),
    path('estrategia/update/<int:pk>/', views.estrategia_update, name='estrategia_update'),
    path('estrategia/delete/<int:pk>/', views.estrategia_delete, name='estrategia_delete'),

    # Rutas para el modelo Evento
    path('evento/', views.evento_list, name='evento_list'),
    path('evento/<int:pk>/', views.evento_detail, name='evento_detail'),
    path('evento/create/', views.evento_create, name='evento_create'),
    path('evento/update/<int:pk>/', views.evento_update, name='evento_update'),
    path('evento/delete/<int:pk>/', views.evento_delete, name='evento_delete'),

    # Rutas para el modelo Profesor
    path('profesor/', views.profesor_list, name='profesor_list'),
    path('profesor/<int:pk>/', views.profesor_detail, name='profesor_detail'),
    path('profesor/create/', views.profesor_create, name='profesor_create'),
    path('profesor/update/<int:pk>/', views.profesor_update, name='profesor_update'),
    path('profesor/delete/<int:pk>/', views.profesor_delete, name='profesor_delete'),

    # Rutas para el modelo Reporte
    path('reporte/', views.reporte_list, name='reporte_list'),
    path('reporte/<int:pk>/', views.reporte_detail, name='reporte_detail'),
    path('reporte/create/', views.reporte_create, name='reporte_create'),
    path('reporte/update/<int:pk>/', views.reporte_update, name='reporte_update'),
    path('reporte/delete/<int:pk>/', views.reporte_delete, name='reporte_delete'),

    # Rutas para el modelo RegistroUsuario
    path('registro_usuario/', views.registro_usuario_list, name='registro_usuario_list'),
    path('registro_usuario/<int:pk>/', views.registro_usuario_detail, name='registro_usuario_detail'),
    path('registro_usuario/create/', views.registro_usuario_create, name='registro_usuario_create'),
    path('registro_usuario/update/<int:pk>/', views.registro_usuario_update, name='registro_usuario_update'),
    path('registro_usuario/delete/<int:pk>/', views.registro_usuario_delete, name='registro_usuario_delete'),

    # Rutas para el modelo Encuesta
    path('encuesta/', views.encuesta_list, name='encuesta_list'),
    path('encuesta/<int:pk>/', views.encuesta_detail, name='encuesta_detail'),
    path('encuesta/create/', views.encuesta_create, name='encuesta_create'),
    path('encuesta/update/<int:pk>/', views.encuesta_update, name='encuesta_update'),
    path('encuesta/delete/<int:pk>/', views.encuesta_delete, name='encuesta_delete'),
    path('encuestas/crear/', views.encuesta_create, name='encuesta_create'),
]
