from django.db import models
from languages.fields import LanguageField


# Create your models here.
class Schedule(models.Model):
    CINEMAS = ((i, i) for i in range(1, 25))
    TYPES = (
        ('3D', '3D'),
        ('4D', '4D'),
        ('Tradicional', 'Tradicional'),
        ('IMAX', 'IMAX')
    )

    schedule = models.DateTimeField(auto_now=False, auto_now_add=False, null=False, blank=False)
    cinema = models.IntegerField(choices=(CINEMAS), null=False, blank=False)
    language = LanguageField(null=False, blank=False)
    cinema_type = models.CharField(choices=(TYPES), max_length=20, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    movie = models.ForeignKey("movie.Movie", on_delete=models.CASCADE, null=False, blank=False)

class Seat(models.Model):
    ROWS = ((chr(i), chr(i)) for i in range(ord('A'),ord('O')+1))
    COLUMNS = ((i, i) for i in range(1, 50))

    row = models.CharField(choices=(ROWS), max_length=1, null=False, blank=False)
    column = models.IntegerField(choices=(COLUMNS), null=False, blank=False)
    schedule = models.ForeignKey("cinema.Schedule", on_delete=models.CASCADE, null=False, blank=False)

