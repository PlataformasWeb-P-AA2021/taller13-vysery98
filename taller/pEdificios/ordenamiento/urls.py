"""
    Manejo de urls para la aplicación
    ordenamiento
"""
from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage

# Se importa las vistas de la aplicación
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Edificios
    path('edificio/<int:id>', views.obtener_edificio, 
        name='obtener_edificio'),
    path('crear/edificio', views.crear_edificio, 
        name='crear_edificio'),
    path('editar_edificio/<int:id>', views.editar_edificio, 
        name='editar_edificio'),
    path('eliminar/edificio/<int:id>', views.eliminar_edificio, 
        name='eliminar_edificio'),
    # Departamentos
    path('crear/departamentos', views.crear_departamento, 
        name='crear_departamento'),
    path('editar/departamento/<int:id>', views.editar_departamento, 
        name='editar_departamento'),
    path('eliminar/departamento/<int:id>', views.eliminar_departamento, 
        name='eliminar_departamento'),
    # Departamento de un edificio
    path('crear/departamento/edificio/<int:id>', views.crear_departamento_edificio, 
        name='crear_departamento_edificio'),
]
