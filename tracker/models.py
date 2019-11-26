from django.conf import settings
from django.contrib.auth import get_user_model 
from django.db import models
from django.urls import reverse
import os
import uuid
from datetime import datetime
from .parse import parse_datafile


def uuid_filename(instance, filename):
    ext = filename.split(".")[-1]
    id = uuid.uuid4()
    filename = f"${id}.${ext}"
    return os.path.join("img", filename)

class Museum(models.Model):
    institution = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    def __str__(self): return self.institution

class SensorType(models.Model):
    type = models.CharField(max_length=150)
    model = models.CharField(max_length=150)

    def __str__(self): return self.type + " " + self.model

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

    def __str__(self): return self.name

class Location(models.Model):
    museum = models.ForeignKey(
        'Museum',
        on_delete=models.CASCADE,
    )
    room = models.CharField(max_length=150) 

    def __str__(self): return self.room

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