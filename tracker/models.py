from django.conf import settings
from django.contrib.auth import get_user_model 
from django.db import models
from django.urls import reverse
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField

class Museum(models.Model):
    institution = models.CharField(max_length=150, help_text="Please enter the name of your institution")
    city = models.CharField(max_length=100, help_text="Please enter the city in which your insitution is located")
    YOUR_STATE_CHOICES = list(STATE_CHOICES)
    YOUR_STATE_CHOICES.insert(0, ('', '-------'))
    state = USStateField(choices=STATE_CHOICES, help_text="Please choose the state in which your institution is located from the provided list")
  
    def __str__(self): return self.institution

class SensorType(models.Model):
    type = models.CharField(max_length=150, help_text="Please describe the brand of the sensor you have (ie Raspberry Pi)")
    model = models.CharField(max_length=150, help_text="Please describe the model of the sensor you have (ie 2.0)")

    def __str__(self): return self.type + " " + self.model

class Sensor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, help_text="Please give your sensor a unique name to distinguish it from other sensors you may have")
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

    def __str__(self): return self.name

class Location(models.Model):
    museum = models.ForeignKey(
        'Museum',
        on_delete=models.CASCADE,
    )
    room = models.CharField(max_length=150, help_text="Please describe the room in which the sensor is located") 

    def __str__(self): return self.room