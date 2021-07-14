from django.urls import path
from rest_framework.routers import DefaultRouter

from app.agronomia.api_views import ProjectViewSet, SequimientoViewSet, CountPlant

routers = DefaultRouter()
routers.register(r"plantas", ProjectViewSet)
routers.register(r"seguimiento", SequimientoViewSet)
urlpatterns = [
    path("countPlant/", CountPlant.as_view()),
]
urlpatterns += routers.urls
