from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class formularioRegistro(forms.Form):
    Email = forms.CharField(label="email", max_length=255)
    Rut = forms.CharField(label="rut", max_length=255)
    Nombres = forms.CharField(label="nombres", max_length=255)
    Apellidos = forms.CharField(label="apellidos", max_length=255)
    Dia = forms.CharField(label="fecha", max_length=2)
    Mes = forms.CharField(label="fecha", max_length=2)
    Anno = forms.CharField(label="fecha", max_length=2)
    Telefono = forms.CharField(label="telefono", max_length=9)
    Region = forms.CharField(label="region", max_length=255)
    Comuna = forms.CharField(label="comuna", max_length=255)
    TipoViaje = forms.CharField(label="tipo", max_length=255)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(UserCreationForm):

    class Meta:
        model = User
        fields= ['email', 'password1']
        
