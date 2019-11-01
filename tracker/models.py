from django.conf import settings
from django.contrib.auth import get_user_model 
from django.db import models
from django.urls import reverse

class Museum(models.Model):
    institution = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

class SensorType(models.Model):
    type = models.CharField(max_length=150)
    model = models.CharField(max_length=150)

class Sensor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
    )
    museum = models.ForeignKey(
        'Museum',
        on_delete=models.CASCADE,
    )
    sensortype = models.ForeignKey(
        'SensorType',
        on_delete=models.CASCADE,
    )

class Location(models.Model):
    museum = models.ForeignKey(
        'Museum',
        on_delete=models.CASCADE,
    )
    room = models.CharField(max_length=150) 