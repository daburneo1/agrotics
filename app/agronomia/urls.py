"""agrotics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from app.agronomia.views import (BaseView, IndexView, PlantView, NewPlantView, SeguimientoView, TaxonomiaView,
                                 CuidadoView, RiegoView, PlantacionView, SemilleroView, SueloView,
                                 HumedadView, MorfologiaView,
                                 TemperaturaView, CategoriaView, PlantUpdateView, PlantDeleteView, NewSeguimientoView,
                                 DatosFenologicosCultivoView, DatosFertilizanteView, DatosClimaView,
                                 DatosAnalisisSueloView, DatosControlPlagasView, DatosUbicacionView, VariedadesView,
                                 SeguimientoDeleteView, SeguimientoUpdateView, ValorNutricionalView, ZonaProduccionView,
                                 EpocaSiembraView, PlagasEnfermedadesView, LogoutSession,
                                 )

urlpatterns = [
                  path("base", BaseView.as_view(), name='base'),
                  path("", IndexView.as_view(), name='index'),
                  path("planta/", PlantView.as_view(), name='plant_list'),
                  path('planta/edit/<int:pk>', PlantUpdateView.as_view(), name='plant_update'),
                  path('planta/delete/<int:pk>', PlantDeleteView.as_view(), name='plant_delete'),
                  path("seguimiento/", SeguimientoView.as_view(), name='seguimiento_list'),
                  path('seguimiento/edit/<int:pk>', SeguimientoUpdateView.as_view(), name='seguimiento_update'),
                  path('seguimiento/delete/<int:pk>', SeguimientoDeleteView.as_view(), name='seguimiento_delete'),
                  path("nueva_plantas/", NewPlantView.as_view(), name='nuevaPlanta'),
                  path("nueva_seguimientos/", NewSeguimientoView.as_view(), name='nuevaSeguimiento'),
                  path("nueva_taxonomia/", TaxonomiaView.as_view(), name='idTaxonomia'),
                  path("nueva_cuidado/", CuidadoView.as_view(), name='idCuidado'),
                  path("nueva_riego/", RiegoView.as_view(), name='idRiego'),
                  path("nueva_plantacion/", PlantacionView.as_view(), name='idPlantacion'),
                  path("nueva_semillero/", SemilleroView.as_view(), name='idSemillero'),
                  path("nueva_suelo/", SueloView.as_view(), name='idSuelo'),
                  path("nueva_humedad/", HumedadView.as_view(), name='idHumedad'),
                  path("nueva_morfologia/", MorfologiaView.as_view(), name='idMorfologia'),
                  path("nueva_temperatura/", TemperaturaView.as_view(), name='idTemperatura'),
                  path("nueva_categoria/", CategoriaView.as_view(), name='idCategoria'),
                  path("nueva_nutricional/", ValorNutricionalView.as_view(), name='idValorNutricional'),
                  path("nueva_zona_produccion/", ZonaProduccionView.as_view(), name='idZonaProduccion'),
                  path("nueva_epoca_siembra/", EpocaSiembraView.as_view(), name='idEpocaSiembra'),
                  path("nueva_plagas_enfermedades/", PlagasEnfermedadesView.as_view(), name='idPlagasEnfermedades'),
                  path("nueva_variedades/", VariedadesView.as_view(), name='idVariedad'),
                  path("nueva_datosfenologicos/", DatosFenologicosCultivoView.as_view(),
                       name='idDatosFenologicosCultivo'),
                  path("nueva_datosfertilizante/", DatosFertilizanteView.as_view(), name='idDatosFertilizante'),
                  path("nueva_datosclima/", DatosClimaView.as_view(), name='idDatosClima'),
                  path("nueva_datosanalisisSuelo/", DatosAnalisisSueloView.as_view(), name='idDatosAnalisisSuelo'),
                  path("nueva_datoscontrolplagas/", DatosControlPlagasView.as_view(), name='idDatosControlPlagas'),
                  path("nueva_datosubicacion/", DatosUbicacionView.as_view(), name='idDatosUbicacion'),
                  path("nueva_plantas/", NewPlantView.as_view(), name='idPlanta'),
                  path("nueva_variedades/", VariedadesView.as_view(), name='idVariedades'),
                  path("logout/", LogoutSession.as_view(), name="logout"),
                  path('accounts/', include('django.contrib.auth.urls'), name="login"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
