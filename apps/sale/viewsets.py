from rest_framework import viewsets
from .models import Sale
from apps.cinema.models import Schedule,Seat
from .serializer import SaleSerializer
from django.contrib.auth.models import User

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleMovieUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def get_queryset(self):
        #Selected movie
        movie_id = self.request.query_params.get('movie_id', None)

        #Get all objects from Seat
        queryset = Sale.objects.all()

        #Client
        user_id = self.request.query_params.get('user_id', None)
        if not User.objects.filter(id=user_id).exists():
            return queryset.none()

        #Filtering with movie title
        if movie_id is not None:
            if Schedule.objects.select_related("movie").filter(movie_id=movie_id).exists():
                schedule = Schedule.objects.select_related("movie").get(movie_id=movie_id)
                seat = Seat.objects.filter(schedule_id=schedule.id)
                queryset = queryset.filter(seat_id=seat.id, user_id=user_id)
            else:
                return queryset.none()

        return queryset
