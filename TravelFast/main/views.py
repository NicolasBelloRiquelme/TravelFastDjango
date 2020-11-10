from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .form import CreateUserForm, LoginUserForm, registroForma
from .models import formularioRegistro

# Create your views here.
@login_required(login_url='inicioSesion')
def index(request):
    template = loader.get_template('main/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required(login_url='inicioSesion')
def travels(request):
    template = loader.get_template('main/travels.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required(login_url='inicioSesion')
def notFound(request):
    template = loader.get_template('main/404.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required(login_url='inicioSesion')
def forma(request):
    data = {
        'form': registroForma(request.POST or None)
    }

    if request.method == 'POST':
        formulario = registroForma(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Formulario Enviado"
            return redirect('index')
        else:
            data["form"] = formulario
    else:
        formulario = registroForma()
    
    return render(request, 'main/forma.html', data)


def crearUsuario(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']

                user = authenticate(email=email, password=password)
                login(request, user)

                messages.success(request,"Usuario Creado Exitosamente!")

                return redirect('inicioSesion')
        else:
            form = CreateUserForm()

    context = {'form':form}
    return render(request, 'main/crearUsuario.html', context)

def inicioSesion(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Usuario o Contraseña Incorrectos')
    
    context = {}
    return render(request, 'main/inicioSesion.html', context)

@login_required(login_url='inicioSesion')
def salirSesion(request):
    logout(request)
    return redirect('inicioSesion')

@login_required(login_url='inicioSesion')
def mostrarForma(request):
    all_data = formularioRegistro.objects.all
    return render(request, 'main/mostrarForma.html', {'all':all_data})