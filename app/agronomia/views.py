from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, FormView, DeleteView, UpdateView, CreateView, ListView

from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from app.agronomia.forms import PlantaForm, TaxonomiaForm, CuidadoForm, RiegoForm, PlantacionForm, \
    SemilleroForm, SueloForm, HumedadForm, MorfologiaForm, TemperaturaForm, CategoriaForm, SeguimientoForm, \
    DatosFenologicosCultivoForm, DatosFertilizanteForm, DatosClimaForm, DatosAnalisisSueloForm, DatosControlPlagasForm, \
    DatosUbicacionForm, VariedadesForm, ValorNutricionalForm, ZonaProduccionForm, EpocaSiembraForm, \
    PlagasEnfermedadesForm
from app.agronomia.models import Planta, DatosCultivo


class BaseView(TemplateView):
    template_name = "base.html"


class IndexView(TemplateView):
    template_name = "internas/index.html"


class PlantView(ListView):
    model = Planta
    template_name = "internas/planta.html"


class SeguimientoView(ListView):
    model = DatosCultivo
    template_name = "internas/seguimiento.html"


class NewPlantView(CreateView):
    template_name = "internas/form.html"
    form_class = PlantaForm
    success_url = "/nueva_plantas/"


class NewSeguimientoView(CreateView):
    template_name = "internas/form.html"
    form_class = SeguimientoForm
    success_url = "/seguimiento/"


class TaxonomiaView(CreateView):
    template_name = "internas/form.html"
    success_url = "/nueva_plantas/"
    form_class = TaxonomiaForm


class CuidadoView(CreateView):
    template_name = "internas/form.html"
    form_class = CuidadoForm
    success_url = "/nueva_plantas/"


class RiegoView(CreateView):
    template_name = "internas/form.html"
    form_class = RiegoForm
    success_url = "/nueva_plantas/"


class PlantacionView(CreateView):
    template_name = "internas/form.html"
    form_class = PlantacionForm
    success_url = "/nueva_plantas/"


class SemilleroView(CreateView):
    template_name = "internas/form.html"
    form_class = SemilleroForm
    success_url = "/nueva_plantas/"


class SueloView(CreateView):
    template_name = "internas/form.html"
    form_class = SueloForm
    success_url = "/nueva_plantas/"


class HumedadView(CreateView):
    template_name = "internas/form.html"
    form_class = HumedadForm
    success_url = "/nueva_plantas/"


class MorfologiaView(CreateView):
    template_name = "internas/form.html"
    form_class = MorfologiaForm
    success_url = "/nueva_plantas/"


class TemperaturaView(CreateView):
    template_name = "internas/form.html"
    form_class = TemperaturaForm
    success_url = "/nueva_plantas/"


class CategoriaView(CreateView):
    template_name = "internas/form.html"
    form_class = CategoriaForm
    success_url = "/nueva_plantas/"

class ValorNutricionalView(CreateView):
    template_name = "internas/form.html"
    form_class = ValorNutricionalForm
    success_url = "/nueva_plantas"

class DatosFenologicosCultivoView(CreateView):
    template_name = "internas/form.html"
    form_class = DatosFenologicosCultivoForm
    success_url = "/nueva_seguimientos/"


class DatosAnalisisSueloView(CreateView):
    template_name = "internas/form.html"
    form_class = DatosAnalisisSueloForm
    success_url = "/nueva_seguimientos/"


class DatosControlPlagasView(CreateView):
    template_name = "internas/form.html"
    form_class = DatosControlPlagasForm
    success_url = "/nueva_seguimientos/"


class DatosUbicacionView(CreateView):
    template_name = "internas/form.html"
    form_class = DatosUbicacionForm
    success_url = "/nueva_seguimientos/"


class VariedadesView(CreateView):
    template_name = "internas/form.html"
    form_class = VariedadesForm
    success_url = "/nueva_seguimientos/"


class DatosClimaView(CreateView):
    template_name = "internas/form.html"
    form_class = DatosClimaForm
    success_url = "/nueva_seguimientos/"


class DatosFertilizanteView(CreateView):
    template_name = "internas/form.html"
    form_class = DatosFertilizanteForm
    success_url = "/nueva_seguimientos/"

class ZonaProduccionView(CreateView):
    template_name = "internas/form.html"
    form_class = ZonaProduccionForm
    success_url = "/nueva_seguimientos/"

class EpocaSiembraView(CreateView):
    template_name = "internas/form.html"
    form_class = EpocaSiembraForm
    success_url = "/nueva_seguimientos/"

class PlagasEnfermedadesView(CreateView):
    template_name = "internas/form.html"
    form_class = PlagasEnfermedadesForm
    success_url = "/nueva_seguimientos/"

class PlantUpdateView(UpdateView):
    model = Planta
    form_class = PlantaForm
    template_name = "internas/form.html"
    success_url = reverse_lazy('plant_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            form = self.get_form()
            if action == 'edit':
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de planta'
        context['list_url'] = reverse_lazy('plant_list')
        context['action'] = 'edit'
        return context



class SeguimientoUpdateView(UpdateView):
    model = DatosCultivo
    form_class = SeguimientoForm
    template_name = "internas/form.html"
    success_url = reverse_lazy('seguimiento_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            form = self.get_form()
            if action == 'edit':
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de seguimiento'
        context['list_url'] = reverse_lazy('seguimiento_list')
        context['action'] = 'edit'
        return context


class PlantDeleteView(DeleteView):
    model = Planta
    template_name = 'internas/delete.html'
    form_class = PlantaForm
    success_url = reverse_lazy('plant_list')

    def get_context_data(self, **kwargs):
        print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar planta'
        context['list_url'] = reverse_lazy('plant_list')
        return context


class SeguimientoDeleteView(DeleteView):
    model = DatosCultivo
    template_name = 'internas/delete.html'
    form_class = SeguimientoForm
    success_url = reverse_lazy('seguimiento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar seguimiento'
        context['list_url'] = reverse_lazy('seguimiento_list')
        return context
