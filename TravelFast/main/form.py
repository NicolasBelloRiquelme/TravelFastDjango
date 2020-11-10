from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import formularioRegistro




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUserForm(UserCreationForm):

    class Meta:
        model = User
        fields= ['email', 'password1']
        
class registroForma(forms.ModelForm):
    Region = forms.CharField(widget=forms.TextInput())
    Comuna = forms.CharField(widget=forms.TextInput())
    TipoViaje = forms.CharField(widget=forms.TextInput())
    
    class Meta:
        model = formularioRegistro
        fields = ["Email", "Rut", "Nombres", "Apellidos", "Telefono", "Region", "Comuna", "TipoViaje", "Imagen"]

