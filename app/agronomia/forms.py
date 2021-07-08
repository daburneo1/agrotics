from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.forms import ModelForm, Textarea, TextInput, FileInput

from app.agronomia.models import Planta, Riego, Taxonomia, Cuidado, Plantacion, Semillero, Suelo, Humedad, Morfologia, \
    Temperatura, Categoria, DatosCultivo, DatosFenologicosCultivo, DatosFertilizante, DatosClima, DatosAnalisisSuelo, \
    DatosControlPlagas, DatosUbicacion, Variedades, ValorNutricional


class PlantaForm(ModelForm):
    class Meta:
        model = Planta
        fields = "__all__"


class TaxonomiaForm(ModelForm):
    class Meta:
        model = Taxonomia
        fields = "__all__"

class ValorNutricionalForm(ModelForm):
    class Meta:
        model = ValorNutricional
        fields = "__all__"


class DatosClimaForm(ModelForm):
    class Meta:
        model = DatosClima
        fields = "__all__"


class DatosAnalisisSueloForm(ModelForm):
    class Meta:
        model = DatosAnalisisSuelo
        fields = "__all__"


class DatosControlPlagasForm(ModelForm):
    class Meta:
        model = DatosControlPlagas
        fields = "__all__"


class DatosUbicacionForm(ModelForm):
    class Meta:
        model = DatosUbicacion
        fields = "__all__"


class VariedadesForm(ModelForm):
    class Meta:
        model = Variedades
        fields = "__all__"


class DatosFenologicosCultivoForm(ModelForm):
    class Meta:
        model = DatosFenologicosCultivo
        fields = "__all__"


class DatosFertilizanteForm(ModelForm):
    class Meta:
        model = DatosFertilizante
        fields = "__all__"


class SeguimientoForm(ModelForm):
    class Meta:
        model = DatosCultivo
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
