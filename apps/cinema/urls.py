from rest_framework import routers
from .viewsets import ScheduleViewSet, SeatViewSet
from django.conf.urls import url

#Rutas
router = routers.SimpleRouter()
router.register('schedules', ScheduleViewSet)
router.register('seats',SeatViewSet)

urlpatterns = [
    url(r'^schedules/(?P<movie_id>\d+)/$', ScheduleViewSet.as_view({'get': 'list'})),
    url(r'^seats/(?P<schedule_id>\d+)/$', SeatViewSet.as_view({'get': 'list'})),
] + router.urls