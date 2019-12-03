from django.urls import path
from .views import (
    SubmissionListView,
    SubmissionDetailView,
)

urlpatterns = [
    path("submission_list/", SubmissionListView.as_view(), name="submission_list"),
    path("submission/<int:pk>/", SubmissionDetailView.as_view(), name="submission_detail"),
]