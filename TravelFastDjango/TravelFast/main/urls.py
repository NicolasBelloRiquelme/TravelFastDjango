from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('travels', views.travels, name='travels'),
    path('404', views.notFound, name='404'),
    path('forma', views.forma, name='forma'),
    path('loginForma', views.loginForma, name='loginForma'),
    path('crearLogin', views.crearLogin, name='crearLogin')
]