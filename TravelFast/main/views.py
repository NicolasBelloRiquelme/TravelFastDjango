from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login

# Create your views here.
def landingPage(request):
    return HttpResponse("Bienvenido")

def index(request):
    template = loader.get_template('main/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def travels(request):
    template = loader.get_template('main/travels.html')
    context = {}
    return HttpResponse(template.render(context, request))

def loginForma(request):
    template = loader.get_template('main/loginForma.html')
    context = {}
    return HttpResponse(template.render(context, request))

def notFound(request):
    template = loader.get_template('main/404.html')
    context = {}
    return HttpResponse(template.render(context, request))

def forma(request):
    template = loader.get_template('main/forma.html')
    context = {}
    return HttpResponse(template.render(context, request))

def crearLogin(request):
    template = loader.get_template('main/crearLogin.html')
    context = {}
    return HttpResponse(template.render(context, request))

