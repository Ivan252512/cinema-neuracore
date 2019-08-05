from rest_framework import routers
from .viewsets import SaleViewSet, SaleMovieUserViewSet
from django.conf.urls import url

#Rutas
router = routers.SimpleRouter()
router.register('sales',SaleViewSet)
router.register('sales_movie_user', SaleMovieUserViewSet)

urlpatterns = [
    url(r'^sales_movie_user/(?P<movie_id>\d+)/$', SaleMovieUserViewSet.as_view({'get': 'list'})),
] + router.urls