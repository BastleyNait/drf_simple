from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()
#primero va el nombre de la ruta, la api, el nombre
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls

