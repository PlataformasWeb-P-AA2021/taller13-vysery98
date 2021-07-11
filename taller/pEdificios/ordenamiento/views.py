from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
# Importación de las clases de modelos.py y formularios.py
from ordenamiento.models import *
from ordenamiento.forms import *
# Uso de django-rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from ordenamiento.serializers import UserSerializer, GroupSerializer, EdificioSerializer, DepartamentoSerializer

# Create your views here.

def index(request):
    """
        Listar los registros del modelo Edificio,
        obtenidos de la base de datos.
    """
    edificios = Edificio.objects.all()
    informacion_template = {'edificios': edificios, 'numero_edificios': len(edificios)}
    return render(request, 'index.html', informacion_template)

# CRUD - EDIFICIO
def obtener_edificio(request, id):
    """
        Listar los registros del modelo Edificio,
        obtenidos de la base de datos.
    """
    edificios = Edificio.objects.get(pk=id)
    informacion_template = {'edificios': edificios}
    return render(request, 'obtener_edificio.html', informacion_template)

def crear_edificio(request):
    if request.method=='POST':
        formulario = EdificioForm(request.POST)
        print(formulario.errors)
        
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm()
    
    diccionario = {'formulario': formulario}
    return render(request, 'crearEdificio.html', diccionario)

def editar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)

    diccionario = {'formulario': formulario}
    return render(request, 'editarEdificio.html', diccionario)

def eliminar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)

# CRUD - DEPARTAMENTO
def crear_departamento(request):
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm()

    diccionario = {'formulario': formulario}
    return render(request, 'crearDepartamento.html', diccionario)

def editar_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm(instance=departamento)

    diccionario = {'formulario': formulario}
    return render(request, 'editarDepartamento.html', diccionario)

def eliminar_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)

# CREACIÓN DE UN DEPARTAMENTO A UN EDIFICIO INDICADO
def crear_departamento_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoEdificioForm(edificio, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoEdificioForm(edificio)

    diccionario = {'formulario': formulario, 'edificio': edificio}
    return render(request, 'crearDepartamentoEdificio.html', diccionario)

# Views de Serializers (Viewsets)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]