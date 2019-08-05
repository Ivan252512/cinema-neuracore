from django.db import models

# Create your models here.

class Movie(models.Model):
    CLASSIFICATIONS = (
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC-17', 'NC-17')
    )
    CATEGORIES = (
        ('Acción', 'Acción'),
        ('Aventura', 'Aventura'),
        ('Comedia', 'Comedia'),
        ('Crimen y mafia', 'Crimen y mafia'),
        ('Darama', 'Darama'),
        ('Historia', 'Historia'),
        ('Horror', 'Horror'),
        ('Musicales', 'Musicales'),
        ('Ciencia ficción', 'Ciencia ficción'),
        ('Guerra', 'Guerra'),
        ('Westerns', 'Westerns')
    )

    title = models.CharField(max_length=60, null=False, blank=False)
    synopsis = models.TextField(null=False, blank=False)
    classification = models.CharField(choices=(CLASSIFICATIONS), max_length=5)
    category = models.CharField(choices=(CATEGORIES), max_length=20)
    release = models.DateTimeField(auto_now=False, auto_now_add=False, null=False, blank=False)
    length  = models.TimeField(auto_now=False, auto_now_add=False, null=False, blank=False)