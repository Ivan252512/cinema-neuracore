from rest_framework import routers
from .viewsets import UserViewSet

#Rutas
router = routers.SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = router.urls