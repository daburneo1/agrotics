from rest_framework import viewsets

from app.agronomia.models import Planta
from app.agronomia.serializer import PlantaSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer



