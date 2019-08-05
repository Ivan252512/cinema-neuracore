from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sale(models.Model):
    seat = models.OneToOneField("cinema.Seat", on_delete=models.CASCADE, null=False, blank=False)
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
