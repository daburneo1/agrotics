from rest_framework import serializers

from app.agronomia.models import Planta, Taxonomia, Cuidado, Riego, Plantacion, Semillero, Suelo, Humedad, Morfologia, \
    Temperatura, Categoria


class TaxonomiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomia
        fields = "__all__"


class CuidadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuidado
        fields = "__all__"


class RiegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riego
        fields = "__all__"


class PlantacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantacion
        fields = "__all__"


class SemilleroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semillero
        fields = "__all__"


class SueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suelo
        fields = "__all__"


class HumedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humedad
        fields = "__all__"


class MorfologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morfologia
        fields = "__all__"


class TemperaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperatura
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class PlantaSerializer(serializers.ModelSerializer):
    idTaxonomia = TaxonomiaSerializer()
    idCuidado = CuidadoSerializer()
    idRiego = RiegoSerializer()
    idPlantacion = PlantacionSerializer()
    idSemillero = SemilleroSerializer()
    idSuelo = SueloSerializer()
    idHumedad = HumedadSerializer()
    idMorfologia = MorfologiaSerializer()
    idTemperatura = TemperaturaSerializer()
    idCategoria = CategoriaSerializer()

    class Meta:
        model = Planta
        fields = [
            "imagen", "cicloVida", "origen", "usoAplicacion",
            "produccionPromedio", "altura",
            "diametro", "clima", "preparacionTerreno",
            "qr", "fechaIngreso", "idTaxonomia",
            "idCuidado", "idRiego", "idPlantacion",
            "idSemillero", "idSuelo", "idHumedad", "idMorfologia"
            , "idTemperatura", "idCategoria"
        ]
