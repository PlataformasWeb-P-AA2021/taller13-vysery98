from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from ordenamiento.models import Edificio, Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo_edificio']
        labels = {
            'nombre': _('Ingrese el nombre del edificio'),
            'direccion': _('Dirección del edificio'),
            'ciudad': _('Ingrese la ciudad'),
            'tipo_edificio': _('Seleccione el tipo de edificio'),
        }

    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())
        # num_palabras < 1 - comprueba que el campo no esté vacío
        if num_palabras < 1:
            raise forms.ValidationError("Ingrese el nombre del edificio")
        return valor

    def clean_direccion(self):
        valor = self.cleaned_data['direccion']
        num_palabras = len(valor.split())
        # num_palabras < 1 - comprueba que el campo no esté vacío
        if num_palabras < 1:
            raise forms.ValidationError("Ingrese la dirección")
        return valor

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        num_palabras = len(valor.split())
        # num_palabras < 1 - comprueba que el campo no esté vacío
        if num_palabras < 1:
            raise forms.ValidationError("Ingrese la ciudad")
        return valor

    def clean_tipo_edificio(self):
        valor = self.cleaned_data['tipo_edificio']
        if len(valor) < 1:
            raise forms.ValidationError("Seleccione un tipo de edificio")
        return valor

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'num_cuartos', 'edificio']

    def clean_propietario(self):
        valor = self.cleaned_data['propietario']
        num_palabras = len(valor.split())
        # El nombre completo de un propietario no debe tener menos de 3 palabras.
        if num_palabras < 3:
            raise forms.ValidationError("Ingrese los nombres completo")
        return valor

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        # Costo de un departamento no puede ser menor a $0
        if valor < 0:
            raise forms.ValidationError("El costo ingresado no es válido")
        return valor

    def clean_num_cuartos(self):
        valor = self.cleaned_data['num_cuartos']
        # Número de cuartos no puede ser menor o igual que 0
        if valor <= 0:
            raise forms.ValidationError("Ingrese un número de cuartos válido")
        return valor

class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'num_cuartos', 'edificio']

    def clean_propietario(self):
        valor = self.cleaned_data['propietario']
        num_palabras = len(valor.split())
        # El nombre completo de un propietario no debe tener menos de 3 palabras.
        if num_palabras < 3:
            raise forms.ValidationError("Ingrese los nombres completo")
        return valor

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        # Costo de un departamento no puede ser menor a $0
        if valor <= 0:
            raise forms.ValidationError("El costo ingresado no es válido")
        return valor

    def clean_num_cuartos(self):
        valor = self.cleaned_data['num_cuartos']
        # Número de cuartos no puede ser menor o igual que 0
        if valor <= 0:
            raise forms.ValidationError("Ingrese un número de cuartos válido")
        return valor
