"""
URL configuration for agroProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from agroApp import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.inicio,name='inicio'),
    path('registro/',views.formulario_registro,name='formulario_registro'),
    path('gestion/login/',views.login_administrador,name='login_administrador'),
    path('gestion/dashboard/',views.dashboard,name='dashboard'),
    path('gestion/agregar/',views.agregar_registro,name='agregar_registro'),
    path('gestion/editar/<int:id>/',views.editar_registro,name='editar_registro'),
    path('gestion/eliminar/<int:id>/',views.eliminar_registro,name='eliminar_registro'),
    path('gestion/logout/',views.cerrar_sesion,name='cerrar_sesion'),
]