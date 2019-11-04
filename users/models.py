from django.contrib.auth.models import AbstractUser 
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=100, null=True, blank=True)
    institution = models.ForeignKey(
        'tracker.Museum',
        on_delete=models.CASCADE,
        null=True, blank=True
    )