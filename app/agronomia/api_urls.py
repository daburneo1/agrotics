from rest_framework.routers import DefaultRouter

from app.agronomia.api_views import ProjectViewSet, SequimientoViewSet

routers = DefaultRouter()
routers.register(r"plantas", ProjectViewSet)
routers.register(r"seguimiento", SequimientoViewSet)
urlpatterns = routers.urls
