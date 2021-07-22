from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, DeleteView, UpdateView, CreateView, ListView

from django.urls import reverse_lazy
from django.http import JsonResponse

from app.agronomia.forms import PlantaForm, TaxonomiaForm, CuidadoForm, RiegoForm, PlantacionForm, \
    SemilleroForm, SueloForm, HumedadForm, MorfologiaForm, TemperaturaForm, CategoriaForm, SeguimientoForm, \
    DatosFenologicosCultivoForm, DatosFertilizanteForm, DatosClimaForm, DatosAnalisisSueloForm, DatosControlPlagasForm, \
    DatosUbicacionForm, VariedadesForm, ValorNutricionalForm, ZonaProduccionForm, EpocaSiembraForm, \
    PlagasEnfermedadesForm
from app.agronomia.models import Planta, DatosCultivo, Variedades


class BaseView(TemplateView):
    template_name = "base.html"


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "internas/index.html"
    redirect_field_name = 'index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            "countPlant": Planta.objects.count(),
            "countSeguimiento": DatosCultivo.objects.count(),
            "countVariedades": Variedades.objects.count()
        })
        return context


class PlantView(LoginRequiredMixin, ListView):
    redirect_field_name = 'plant_list'
    model = Planta
    template_name = "internas/planta.html"


class ZonaProduccionView(LoginRequiredMixin, CreateView):
    template_name = "internas/form.html"
    form_class = ZonaProduccionForm
    success_url = "/nueva_seguimientos/"
    redirect_field_name = 'idZonaProduccion'


class EpocaSiembraView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = EpocaSiembraForm
    success_url = "/nueva_seguimientos/"


class PlagasEnfermedadesView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = PlagasEnfermedadesForm
    success_url = "/nueva_seguimientos/"


class ValorNutricionalView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = ValorNutricionalForm
    success_url = "/nueva_plantas"


class SeguimientoView(LoginRequiredMixin,ListView):
    model = DatosCultivo
    template_name = "internas/seguimiento.html"


class NewPlantView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = PlantaForm
    success_url = "/nueva_plantas/"


class NewSeguimientoView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = SeguimientoForm
    success_url = "/seguimiento/"


class TaxonomiaView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    success_url = "/nueva_plantas/"
    form_class = TaxonomiaForm

class CuidadoView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = CuidadoForm
    success_url = "/nueva_plantas/"


class RiegoView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = RiegoForm
    success_url = "/nueva_plantas/"


class PlantacionView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = PlantacionForm
    success_url = "/nueva_plantas/"


class SemilleroView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = SemilleroForm
    success_url = "/nueva_plantas/"


class SueloView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = SueloForm
    success_url = "/nueva_plantas/"


class HumedadView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = HumedadForm
    success_url = "/nueva_plantas/"


class MorfologiaView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = MorfologiaForm
    success_url = "/nueva_plantas/"


class TemperaturaView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = TemperaturaForm
    success_url = "/nueva_plantas/"


class CategoriaView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = CategoriaForm
    success_url = "/nueva_plantas/"


class DatosFenologicosCultivoView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = DatosFenologicosCultivoForm
    success_url = "/nueva_seguimientos/"


class DatosAnalisisSueloView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = DatosAnalisisSueloForm
    success_url = "/nueva_seguimientos/"


class DatosControlPlagasView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = DatosControlPlagasForm
    success_url = "/nueva_seguimientos/"


class DatosUbicacionView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = DatosUbicacionForm
    success_url = "/nueva_seguimientos/"


class VariedadesView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = VariedadesForm
    success_url = "/nueva_seguimientos/"


class DatosClimaView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = DatosClimaForm
    success_url = "/nueva_seguimientos/"


class DatosFertilizanteView(LoginRequiredMixin,CreateView):
    template_name = "internas/form.html"
    form_class = DatosFertilizanteForm
    success_url = "/nueva_seguimientos/"


class PlantUpdateView(LoginRequiredMixin,UpdateView):
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


class SeguimientoUpdateView(LoginRequiredMixin,UpdateView):
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


class PlantDeleteView(LoginRequiredMixin,DeleteView):
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


class SeguimientoDeleteView(LoginRequiredMixin,DeleteView):
    model = DatosCultivo
    template_name = 'internas/delete.html'
    form_class = SeguimientoForm
    success_url = reverse_lazy('seguimiento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar seguimiento'
        context['list_url'] = reverse_lazy('seguimiento_list')
        return context

class LogoutSession(LogoutView):
    next_page = "login"