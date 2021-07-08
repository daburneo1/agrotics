from rest_framework import viewsets

from app.agronomia.models import Planta, DatosCultivo
from app.agronomia.serializer import PlantaSerializer, SeguimientoSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer


class SequimientoViewSet(viewsets.ModelViewSet):
    queryset = DatosCultivo.objects.all()
    serializer_class = SeguimientoSerializer
