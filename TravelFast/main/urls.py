from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.inicioSesion, name='inicioSesion'),
    path('index', views.index, name='index'),
    path('travels', views.travels, name='travels'),
    path('404', views.notFound, name='404'),
    path('forma', views.forma, name='forma'),
    path('inicioSesion', views.inicioSesion, name='inicioSesion'),
    path('crearUsuario', views.crearUsuario, name='crearUsuario'),
    path('salirSesion', views.salirSesion, name='salirSesion'),
    path('mostrarForma', views.mostrarForma, name='mostrarForma')
]