"""
URL configuration for SGEE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from SGEE.vistas.vistas_generales import login_view, logout_view
from SGEE.vistas import vistas_principal, vistas_usuario
from SGEE.vistas import vistas_usuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('p/pagina_principal/', vistas_principal.estra_view, name='p_pagina_principal'),

    path('p/contactenos/',vistas_principal.contact_view,name='p_contactar'),

    path('p/sobrenos/',vistas_principal.sobrenos_view, name='p_sobrenos'),

    path('p/testimonials/',vistas_principal.visualizarTestimonios, name='p_testimonials'),

    path('pagina_principal/', vistas_usuario.estra_view, name='pagina_principal'),

    path('contactenos/',vistas_usuario.contact_view,name='contactar'),

    path('sobrenos/',vistas_usuario.sobrenos_view, name='sobrenos'),

    path('testimonials/',vistas_usuario.visualizarTestimonios, name='testimonials'),

    path('', include('encuestas.urls')),
    path('', include('grupos.urls')),
    path('', include('profesores.urls')),
    path('', include('estrategias.urls')),
    path('', include('usuarios.urls')),
    path('', include('reportes.urls')),
    path('', include('eventos.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
