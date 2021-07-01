from django.contrib import admin

# Register your models here.
from app.agronomia.models import *


class CategoriaAdmin(admin.ModelAdmin):
    pass


class CuidadoAdmin(admin.ModelAdmin):
    pass


class DatosAnalisisSueloAdmin(admin.ModelAdmin):
    pass


class DatosClimaAdmin(admin.ModelAdmin):
    pass


class DatosControlPlagasAdmin(admin.ModelAdmin):
    pass


class DatosCultivoAdmin(admin.ModelAdmin):
    pass


class DatosFenologicodAdmin(admin.ModelAdmin):
    pass

class PlantaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Cuidado, CuidadoAdmin)
admin.site.register(DatosAnalisisSuelo, DatosAnalisisSueloAdmin)
admin.site.register(DatosClima, DatosClimaAdmin)
admin.site.register(DatosControlPlagas, DatosControlPlagasAdmin)
admin.site.register(DatosCultivo, DatosCultivoAdmin)
admin.site.register(DatosFertilizante, DatosFenologicodAdmin)
admin.site.register(Planta, PlantaAdmin)
