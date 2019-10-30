from django.conf import settings
from django.contrib.auth import get_user_model 
from django.db import models
from django.urls import reverse

class Museums(models.Model):
    institution = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    )
def __str__(self): 
    return self.institution

class SensorType(models.Model):
    type = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    )
def __str__(self): 
    return self.type
    return self.model