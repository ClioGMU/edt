from django.urls import path
from .views import ( 
    SubmissionListView, 
    SubmissionDetailView, 
    SubmissionCreateView,
    SubmissionDeleteView,
    SensorListView, 
    SensorDetailView, 
    SensorCreateView,
    SensorUpdateView,
    SensorDeleteView,
)

urlpatterns = [
    path('submission/new/', SubmissionCreateView.as_view(), name='submission_new'),
    path('submission/<uuid:pk>/', SubmissionDetailView.as_view(), name='submission_detail'),
    path('submission/<uuid:pk>/delete/', SubmissionDeleteView.as_view(), name='submission_delete'),
    path('submission/list', SubmissionListView.as_view(), name='submission_list'),
    path('sensor/new/', SensorCreateView.as_view(), name='sensor_new'),
    path('sensor/<int:pk>/', SensorDetailView.as_view(), name='sensor_detail'),
    path('sensor/<int:pk>/delete/', SensorDeleteView.as_view(), name='sensor_delete'),
    path('sensor/<int:pk>/edit/', SensorUpdateView.as_view(), name='sensor_edit'),
    path('sensor/list', SensorListView.as_view(), name='sensor_list'),
]