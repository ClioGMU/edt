from django.contrib import admin

from .models import Museum
from .models import SensorType
from .models import Sensor


admin.site.register(Museum)
admin.site.register(SensorType)
admin.site.register(Sensor)
