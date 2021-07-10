from rest_framework import serializers

from app.agronomia.models import Planta, Taxonomia, Cuidado, Riego, Plantacion, Semillero, Suelo, Humedad, Morfologia, \
    Temperatura, Categoria, DatosCultivo, DatosFenologicosCultivo, DatosFertilizante, DatosClima, DatosAnalisisSuelo, \
    DatosControlPlagas, DatosUbicacion, Variedades, ZonaProduccion, PlagasEnfermedades, EpocaSiembra, ValorNutricional


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


class ZonaProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZonaProduccion
        fields = "__all__"


class ValorNutricionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValorNutricional
        fields = "__all__"


class EpocaSiembraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpocaSiembra
        fields = "__all__"


class PlagasEnfermedadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlagasEnfermedades
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
    idValorNutricional = ValorNutricionalSerializer()
    idZonaProduccion = ZonaProduccionSerializer()
    idEpocaSiembra = EpocaSiembraSerializer()
    idPlagasEnfermedades = PlagasEnfermedadesSerializer()

    class Meta:
        model = Planta
        fields = [
            "id", "imagen", "cicloVida", "origen", "usoAplicacion",
            "produccionPromedio", "altura",
            "diametro", "clima", "preparacionTerreno",
            "qr", "fechaIngreso", "idTaxonomia",
            "idCuidado", "idRiego", "idPlantacion",
            "idSemillero", "idSuelo", "idHumedad", "idMorfologia"
            , "idTemperatura", "idCategoria", "idValorNutricional",
            "idZonaProduccion", "idEpocaSiembra", "idPlagasEnfermedades"
        ]


class DatosFenologicosCultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosFenologicosCultivo
        fields = "__all__"


class DatosFertilizanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosFertilizante
        fields = "__all__"


class DatosClimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosClima
        fields = "__all__"


class DatosAnalisisSueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosAnalisisSuelo
        fields = "__all__"


class DatosControlPlagasSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosControlPlagas
        fields = "__all__"


class DatosUbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosUbicacion
        fields = "__all__"


class VariedadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variedades
        fields = "__all__"


class SeguimientoSerializer(serializers.ModelSerializer):
    idDatosFenologicosCultivo = DatosFenologicosCultivoSerializer()
    idDatosFertilizante = DatosFertilizanteSerializer()
    idDatosClima = DatosClimaSerializer()
    idDatosAnalisisSuelo = DatosAnalisisSueloSerializer()
    idDatosControlPlagas = DatosControlPlagasSerializer()
    idDatosUbicacion = DatosUbicacionSerializer()
    idPlanta = PlantaSerializer()
    idVariedades = VariedadesSerializer()

    class Meta:
        model = DatosCultivo
        fields = ["id", "planta", "nombreCientifico", "fechaImplementacion", "idDatosFenologicosCultivo",
                  "idDatosFertilizante", "idDatosClima", "idDatosAnalisisSuelo", "idDatosControlPlagas",
                  "idDatosUbicacion", "idPlanta", "idVariedades"]
