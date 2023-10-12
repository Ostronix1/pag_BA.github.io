"""
URL configuration for web_BA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from banco_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio_web, name='inicio_app'),
    path('registro_voluntario', views.registro_voluntario, name='registro_voluntario'),
    path('pagina-exito/', views.pagina_exito, name='pag_exito'),
    path('registrar_asistencia/', views.registro_asistencia, name='registrar_asistencia'),
    path('exito/', views.exito, name='exito'),
    path('asistencia/', views.ver_asistencia, name="asistencias"),
    path('generar_pdf/', views.generar_pdf, name='generar_pdf'),
    path('ver_voluntario/', views.ver_voluntario, name='voluntario'),




    



]
