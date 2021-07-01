from rest_framework.routers import DefaultRouter

from app.agronomia.api_views import ProjectViewSet

routers = DefaultRouter()
routers.register(r"plantas",ProjectViewSet )
urlpatterns = routers.urls
