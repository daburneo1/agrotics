from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class Morfologia(models.Model):
    semilla = models.CharField(null=True, max_length=100)
    raiz = models.CharField(null=True, max_length=100)
    tallo = models.CharField(null=True, max_length=100)
    hojas = models.CharField(null=True, max_length=100)
    inflorescencia = models.CharField(null=True, max_length=100)
    fruto = models.CharField(null=True, max_length=100)

    def __str__(self):
        _list = [str(self.semilla), str(self.raiz)]
        return " - ".join(list(_list))


class Temperatura(models.Model):
    optima = models.CharField(null=True, max_length=200, blank=True)
    germinacion = models.CharField(null=True, max_length=200, blank=True)
    crecimiento = models.CharField(null=True, max_length=200, blank=True)
    descripcion = models.CharField(null=True, max_length=200)

    def __str__(self):
        _list = [str(self.optima), str(self.germinacion)]
        return " - ".join(list(_list))


class Suelo(models.Model):
    textura = models.CharField(null=True, max_length=200)
    ph = models.CharField(null=True, max_length=45)
    observaciones = models.CharField(null=True, max_length=200)

    def __str__(self):
        _list = [str(self.ph), str(self.textura)]
        return " - ".join(list(_list))


class Humedad(models.Model):
    humedad = models.CharField(null=True, max_length=100)
    observaciones = models.CharField(null=True, max_length=200)

    def __str__(self):
        _list = [str(self.humedad), str(self.observaciones)]
        return " - ".join(list(_list))


class Taxonomia(models.Model):
    nombreComun = models.CharField(null=True, max_length=60, verbose_name="nombre comun")
    familia = models.CharField(null=True, max_length=60)
    genero = models.CharField(null=True, max_length=60)
    especie = models.CharField(null=True, max_length=60)
    nombreCientifico = models.CharField(null=True, max_length=60, unique=True,
                                        verbose_name="nombre cientifico")

    def __str__(self):
        return str(self.nombreComun)


class Cuidado(models.Model):
    abonoFertilizacion = models.CharField(null=True, max_length=100,
                                          verbose_name="abonamiento y fertitlizacion")
    controlMalasHierbas = models.CharField(null=True, max_length=200,
                                           verbose_name="control de malas hierbas")
    recoleccion = models.CharField(null=True, max_length=200,
                                   verbose_name="Recolección")
    almacenamiento = models.CharField(null=True, max_length=200, verbose_name="Almacenamiento")

    def __str__(self):
        return str(self.abonoFertilizacion)


class Semillero(models.Model):
    descripcion = models.CharField(null=True, max_length=200)
    cantidadSemilla = models.CharField(null=True, max_length=100, verbose_name="cantidad de semilla")

    def __str__(self):
        _list = [str(self.descripcion), str(self.cantidadSemilla)]
        return " - ".join(list(_list))


class Plantacion(models.Model):
    detalle = models.CharField(null=True, max_length=300)
    distanciaSurcos = models.CharField(null=True, max_length=100, verbose_name="distancia de los surcos")
    distanciaPlantas = models.CharField(null=True, max_length=100, verbose_name="distancia entre plantas")
    hilerasSurco = models.CharField(null=True, max_length=60, verbose_name="hilera surcos")
    buenaAsociacion = models.CharField(null=True, max_length=100, verbose_name="buena asociacion")
    malaAsociacion = models.CharField(null=True, max_length=100)

    def __str__(self):
        _list = [str(self.distanciaSurcos), str(self.distanciaPlantas)]
        return " - ".join(list(_list))


class Categoria(models.Model):
    categoria = models.CharField(null=True, max_length=500)

    def __str__(self):
        return self.categoria


class Riego(models.Model):
    sistema = models.CharField(null=True, max_length=60)
    detalle = models.CharField(null=True, max_length=200)

    def __str__(self):
        _list = [str(self.sistema), str(self.detalle)]
        return " - ".join(list(_list))


class ValorNutricional(models.Model):
    detalle = models.CharField(null=True, max_length=100)
    valor = models.CharField(null=True, max_length=45)

    def __str__(self):
        return self.detalle


class ZonaProduccion(models.Model):
    nombreRegion = models.CharField(null=True, max_length=45, verbose_name="Región")

    def __str__(self):
        return self.nombreRegion

class EpocaSiembra(models.Model):
    nombreEpoca = models.CharField(null=True, max_length=45, verbose_name="Época")

    def __str__(self):
        return self.nombreEpoca

class PlagasEnfermedades(models.Model):
    nombre = models.CharField(null=True, max_length=100, verbose_name="Plagas y Enfermedades")

    def __str__(self):
        return self.nombre

class Variedades(models.Model):
    variedad = models.CharField(null=True, max_length=150)

    def __str__(self):
        return self.variedad

class Planta(models.Model):
    imagen = models.ImageField(upload_to='images', null=True, blank=True)
    cicloVida = models.CharField(null=True, max_length=45, verbose_name="Ciclo de vida" )
    origen = models.CharField(null=True, max_length=45)
    usoAplicacion = models.CharField(null=True, max_length=1000, verbose_name="Uso y Aplicaciones")
    produccionPromedio = models.CharField(null=True, max_length=100, verbose_name="Producción promedio")
    altura = models.DecimalField(null=True, decimal_places=3, max_digits=10)
    diametro = models.DecimalField(null=True, decimal_places=3, max_digits=10)
    clima = models.CharField(null=True, max_length=45)
    preparacionTerreno = models.CharField(null=True, max_length=1000, verbose_name="Preparación del terreno")
    qr = models.ImageField(upload_to='qr', null=True, blank=True, verbose_name="Código QR")
    fechaIngreso = models.DateField(null=True, verbose_name='Fecha de Ingreso', auto_now=True)
    idTaxonomia = models.ForeignKey(Taxonomia, on_delete=models.CASCADE, null=True,
                                    verbose_name="Taxonomia")
    idCuidado = models.ForeignKey(Cuidado, on_delete=models.CASCADE, null=True, verbose_name="Cuidado")
    idRiego = models.ForeignKey(Riego, on_delete=models.CASCADE, null=True, verbose_name="Riego")
    idPlantacion = models.ForeignKey(Plantacion, on_delete=models.CASCADE, null=True,
                                     verbose_name="Plantacion")
    idSemillero = models.ForeignKey(Semillero, on_delete=models.CASCADE, null=True,
                                    verbose_name="Semillero")
    idSuelo = models.ForeignKey(Suelo, on_delete=models.CASCADE, null=True, verbose_name="Suelo")
    idHumedad = models.ForeignKey(Humedad, on_delete=models.CASCADE, null=True, verbose_name="Humedad")
    idMorfologia = models.ForeignKey(Morfologia, on_delete=models.CASCADE, null=True,
                                     verbose_name="Morfologia")
    idTemperatura = models.ForeignKey(Temperatura, on_delete=models.CASCADE, null=True,
                                      verbose_name="Temperatura")
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True,
                                    verbose_name="Categoria")
    idValorNutricional = models.ForeignKey(ValorNutricional, on_delete=models.CASCADE, null=True,
                                           verbose_name="Valor Nutricional")
    idZonaProduccion = models.ForeignKey(ZonaProduccion, on_delete=models.CASCADE, null=True,
                                         verbose_name="Zona de Producción")
    idEpocaSiembra = models.ForeignKey(EpocaSiembra, on_delete=models.CASCADE, null=True,
                                       verbose_name="Época de Siembra")
    idPlagasEnfermedades = models.ForeignKey(PlagasEnfermedades, on_delete=models.CASCADE, null=True,
                                             verbose_name='Plagas y enfermedades')
    idVariedad = models.ForeignKey(Variedades, on_delete=models.CASCADE, null=True,
                                   verbose_name="Variedad")

    def __str__(self):
        return str(self.idTaxonomia.nombreCientifico)

class RegistroGeneral(models.Model):
    ubicacion = models.CharField(null=True, max_length=45, )
    fechaMuestreo = models.DateField(null=True)
    observaciones = models.CharField(null=True, max_length=45, )


class DatosFertilizante(models.Model):
    fertilizacion = models.CharField(null=True, max_length=100)
    cantidad = models.DecimalField(null=True, decimal_places=3, max_digits=10)
    fechaAplicacion = models.DateField(null=True)


class DatosControlPlagas(models.Model):
    controlPlaga = models.CharField(null=True, max_length=45)
    cantidad = models.DecimalField(null=True, decimal_places=3, max_digits=10)
    fechaAplicacion = models.DateField(null=True)


class DatosClima(models.Model):
    temperatura = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)
    humedad = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)
    riego = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)


class DatosUbicacion(models.Model):
    lote = models.CharField(null=True, max_length=45)
    areaSembrada = models.IntegerField()


class DatosAnalisisSuelo(models.Model):
    ph = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)
    mo = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)
    nitrogeno = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)
    fosforo = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)
    potasio = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)
    otros = models.CharField(null=True, max_length=100, blank=True)


class DatosFenologicosCultivo(models.Model):
    germinacion = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)
    altura = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)
    diametro = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)
    nroRacimo = models.IntegerField(null=True, blank=True)
    nroFloresRacimo = models.IntegerField(null=True, blank=True)
    nroTotalFlores = models.IntegerField(null=True, blank=True)
    nroFrutosRacimo = models.IntegerField(null=True, blank=True)
    nroFrutosTotales = models.IntegerField(null=True, blank=True)
    longitudFruto = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)
    diametroFruto = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)
    pesoFruto = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)
    produccion = models.DecimalField(null=True, decimal_places=3, max_digits=10, blank=True)


class DatosCultivo(models.Model):
    # planta = models.CharField(null=True, max_length=45)
    # nombreCientifico = models.CharField(null=True, max_length=45)
    # fechaImplementacion = models.DateField(null=True)
    idPlanta = models.ForeignKey(Planta, on_delete=models.CASCADE, null=True, verbose_name="Planta")
    idDatosUbicacion = models.ForeignKey(DatosUbicacion, on_delete=models.CASCADE, null=True, verbose_name="Ubicación")
    idDatosFenologicosCultivo = models.ForeignKey(DatosFenologicosCultivo, on_delete=models.CASCADE, null=True,
                                                  verbose_name="Datos Fenológicos")
    idDatosFertilizante = models.ForeignKey(DatosFertilizante, on_delete=models.CASCADE, null=True,
                                            verbose_name="Fertilizante")
    idDatosClima = models.ForeignKey(DatosClima, on_delete=models.CASCADE, null=True, verbose_name="Datos de Clima")
    idDatosAnalisisSuelo = models.ForeignKey(DatosAnalisisSuelo, on_delete=models.CASCADE, null=True,
                                             verbose_name="Análisis del Suelo")
    idDatosControlPlagas = models.ForeignKey(DatosControlPlagas, on_delete=models.CASCADE, null=True,
                                             verbose_name="Control de Plagas")


class Usuario(models.Model):
    nombre = models.CharField(null=True, max_length=45)
    apellido = models.CharField(null=True, max_length=45)
    user = models.CharField(null=True, max_length=45)
    password = models.CharField(null=True, max_length=45)
    idDatosCultivo = models.ForeignKey(DatosCultivo, on_delete=models.CASCADE, null=True)
    idRegistroGeneral = models.ForeignKey(RegistroGeneral, on_delete=models.CASCADE, null=True)
