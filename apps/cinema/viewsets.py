from rest_framework import viewsets
from .models import Schedule, Seat
from apps.movie.models import Movie
from apps.sale.models import Sale
from .serializer import ScheduleSerializer, SeatSerializer
from django.utils import timezone


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        #Selected movie
        movie_id = self.request.query_params.get('movie_id', None)

        #Get all objects from Schedule
        queryset = Schedule.objects.all()

        #Filtering with movie title
        if movie_id is not None:
            if Movie.objects.filter(id=movie_id).exists():
                queryset = queryset.filter(movie_id=movie_id, schedule__gte=timezone.localtime())
            else:
                return queryset.none()

        return queryset

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    def get_queryset(self):
        #Selected movie
        schedule_id = self.request.query_params.get('schedule_id', None)


        #Get all objects from Seat
        queryset = Seat.objects.all()

        #Filtering with movie title
        if schedule_id is not None:
            if Schedule.objects.filter(id=schedule_id).exists():
                schedule = Schedule.objects.get(id=schedule_id)
                queryset = queryset.filter(schedule_id=schedule.id)
                #Unsold tickets
                unsold = []
                for seat in queryset:
                    if not Sale.objects.filter(seat_id=seat).exists():
                        unsold.append(seat)
                return unsold
            else:
                return queryset.none()

        return queryset
