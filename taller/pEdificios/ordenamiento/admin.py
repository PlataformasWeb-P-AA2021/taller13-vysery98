from django.contrib import admin

# Register your models here.
from ordenamiento.models import Edificio, Departamento

# Se crea una clase que hereda de ModelAdmin para
# el modelo Edificio
class EdificioAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo_edificio')
    search_fields = ('nombre', 'ciudad', 'tipo_edificio')

admin.site.register(Edificio, EdificioAdmin)

# Se crea una clase que hereda de ModelAdmin para
# el modelo Departamento
class DepartamentoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    list_display = ('propietario', 'costo', 'num_cuartos', 'edificio')
    # se agrega el atributo raw_id_fields que permite acceder
    # a una interfaz para buscar los estudiantes y seleccionar el
    # que se desee
    raw_id_fields = ('edificio',)

admin.site.register(Departamento, DepartamentoAdmin)