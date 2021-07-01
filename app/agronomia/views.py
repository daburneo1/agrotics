from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, FormView, DeleteView, UpdateView, CreateView, ListView

from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from app.agronomia.forms import PlantaForm, TaxonomiaForm, CuidadoForm, RiegoForm, PlantacionForm, \
    SemilleroForm, SueloForm, HumedadForm, MorfologiaForm, TemperaturaForm, CategoriaForm
from app.agronomia.models import Planta


class BaseView(TemplateView):
    template_name = "base.html"


class IndexView(TemplateView):
    template_name = "internas/index.html"


class PlantView(ListView):
    model = Planta
    template_name = "internas/planta.html"


class SeguimientoView(TemplateView):
    template_name = "internas/seguimiento.html"


class NewPlantView(CreateView):
    template_name = "internas/form.html"
    form_class = PlantaForm
    success_url = "/nueva_plantas/"


# class NewSeguimientoView(CreateView):
#     template_name = "internas/form.html"
#     form_class = SeguimientoForm
#

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
            # data = Planta.objects.get(pk=request.POST['id']).toJSON()
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