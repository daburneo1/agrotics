from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from app.agronomia.models import Planta, DatosCultivo
from app.agronomia.serializer import PlantaSerializer, SeguimientoSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer


class SequimientoViewSet(viewsets.ModelViewSet):
    queryset = DatosCultivo.objects.all()
    serializer_class = SeguimientoSerializer


class CountPlant(APIView):
    def get(self, request):
        countPlant = Planta.objects.count()
        print(countPlant)
        return Response(countPlant)
