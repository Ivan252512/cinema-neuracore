from rest_framework import routers
from .viewsets import MovieViewSet

#Rutas
router = routers.SimpleRouter()
router.register('movies', MovieViewSet)


urlpatterns = router.urls