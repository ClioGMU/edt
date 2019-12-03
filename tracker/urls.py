from django.urls import path
from .views import ( 
    SubmissionListView, 
    SubmissionDetailView, 
    SubmissionCreateView,
    SubmissionDeleteView,
)

urlpatterns = [
    path('submission/new/', SubmissionCreateView.as_view(), name='submission_new'),
    path('submission/<int:pk>/', SubmissionDetailView.as_view(), name='submission_detail'),
    path('submission/<int:pk>/delete/', SubmissionDeleteView.as_view(), name='submission_delete'),
    path('submission/list', SubmissionListView.as_view(), name='submission_list'),
]