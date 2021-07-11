from django.db import models

'''
Entidades: Atributos
- Edificio: nombre, dirección, ciudad, tipo [residencial, comercial]
- Departamento: nombre completo del propietario, costo del departamento,
	número de cuartos, edificio

OBSERVACIÓN: UN DEPARTAMENTO PERTENECE A UN EDIFICIO.
'''
class Edificio(models.Model):
	# Opciones para el atributo 'tipo'
	opciones_tipo = (
	    ('residencial','Residencial'),
	    ('comercial','Comercial'),
    )
    
	nombre = models.CharField("Nombre del edificio", max_length=50)
	direccion = models.CharField("Dirección", max_length=50)
	ciudad = models.CharField("Ciudad", max_length=50)
	tipo_edificio = models.CharField("Tipo", max_length=30, 
        choices=opciones_tipo) 

	def __str__(self):
	    return "%s | %s - %s | %s" % (
            self.nombre,
            self.direccion,
            self.ciudad,
            self.tipo_edificio
        )

# Métodos para obtener información del edificio:
    # Obtención del número total de cuartos
	def obtener_cantidad_cuartos(self):
		valor = [t.num_cuartos for t in self.departamentos.all()]
		valor = sum(valor)

		return valor

    # Obtención del costo total de los departamentos
	def obtener_costo_departamento(self):
		valor = [t.costo for t in self.departamentos.all()]
		valor = sum(valor)

		return valor

class Departamento(models.Model):
	propietario = models.CharField("Propietario/a", max_length=100)
	costo = models.DecimalField(max_digits=100, decimal_places=2)
	num_cuartos = models.IntegerField("Número de cuartos")
	edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
	        related_name="departamentos")

	def __str__(self):
		return "%s | %.2f | %d | %s" % (
            self.propietario, 
			self.costo,
			self.num_cuartos,
			self.edificio
        )
