from django.conf import settings
from django.contrib.auth import get_user_model 
from django.db import models
from django.urls import reverse
import os
import uuid
from datetime import datetime
from .parse import parse_datafile
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField

def uuid_filename(instance, filename):
    ext = filename.split(".")[-1]
    id = uuid.uuid4()
    filename = f"${id}.${ext}"
    return os.path.join("img", filename)

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
    room = models.CharField(max_length=100, help_text="Please describe the location of your sensor")
    museum = models.ForeignKey(
        'Museum',
        on_delete=models.CASCADE,
    )
    sensortype = models.ForeignKey(
        'SensorType',
        on_delete=models.CASCADE,
    )

    def __str__(self): return self.name

class DataPoint(models.Model):
    source = models.ForeignKey('Submission', on_delete=models.PROTECT)
    timestamp = models.DateTimeField(null=False, blank=False)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.pk)

class Submission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(
        'Sensor',
        on_delete=models.CASCADE,
    )
    upload = models.FileField(upload_to="data-files/%Y/%m/%d/", null=True)
    
    def __str__(self): return self.id.__str__()
    
    def get_absolute_url(self):
        return reverse("submission_detail", args=[str(self.id)])

    def save(self, *args, **kwargs):

        print("Now saving...")
        super().save(*args, **kwargs) # Save record of submission

        # Parse the Uploaded Data File
        datapoints = parse_datafile(self.upload.path, self.sensor.sensortype.type)

        # Save the data from data file to the other table
        for point in datapoints:        
            DataPoint.objects.create(
                        source=self, 
                        timestamp = point['timestamp'], 
                        temperature = point['temperature'], 
                        humidity = point['humidity'])        

