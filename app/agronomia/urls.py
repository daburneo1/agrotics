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
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from app.agronomia.views import BaseView, IndexView, PlantView, NewPlantView, SeguimientoView, \
    TaxonomiaView, CuidadoView, RiegoView, PlantacionView, SemilleroView, SueloView, HumedadView, MorfologiaView, \
    TemperaturaView, CategoriaView, PlantUpdateView, PlantDeleteView

urlpatterns = [
                  path("base", BaseView.as_view(), name='base'),
                  path("", IndexView.as_view(), name='index'),
                  path("plantas/", PlantView.as_view(), name='plant_list'),

                  path('plant/edit/<int:pk>', PlantUpdateView.as_view(), name='plant_update'),
                  path('plant/delete/<int:pk>', PlantDeleteView.as_view(), name='plant_delete'),


                  path("seguimiento/", SeguimientoView.as_view(), name='seguimiento_list'),
                  path("nueva_plantas/", NewPlantView.as_view(), name='nuevaPlanta'),
                  # path("nueva_seguimientos/", NewSeguimientoView.as_view(), name='nuevaSeguimiento'),
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
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
