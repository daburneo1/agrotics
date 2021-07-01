from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.forms import ModelForm, Textarea, TextInput, FileInput

from app.agronomia.models import Planta, Riego, Taxonomia, Cuidado, Plantacion, Semillero, Suelo, Humedad, Morfologia, \
    Temperatura, Categoria


class PlantaForm(ModelForm):
    class Meta:
        model = Planta
        fields = "__all__"


class TaxonomiaForm(ModelForm):
    class Meta:
        model = Taxonomia
        fields = "__all__"


class CuidadoForm(ModelForm):
    class Meta:
        model = Cuidado
        fields = "__all__"


class RiegoForm(ModelForm):
    class Meta:
        model = Riego
        fields = "__all__"


class PlantacionForm(ModelForm):
    class Meta:
        model = Plantacion
        fields = "__all__"


class SemilleroForm(ModelForm):
    class Meta:
        model = Semillero
        fields = "__all__"


class SueloForm(ModelForm):
    class Meta:
        model = Suelo
        fields = "__all__"


class HumedadForm(ModelForm):
    class Meta:
        model = Humedad
        fields = "__all__"


class MorfologiaForm(ModelForm):
    class Meta:
        model = Morfologia
        fields = "__all__"


class TemperaturaForm(ModelForm):
    class Meta:
        model = Temperatura
        fields = "__all__"


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"
