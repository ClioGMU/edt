from django.contrib import admin

from .models import Institution
from .models import SensorType
from .models import Sensor
from .models import Submission
from .models import DataPoint

admin.site.register(Institution)
admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(Submission)
admin.site.register(DataPoint)
