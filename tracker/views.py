from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import DataSubmission 

class HomePageView(TemplateView): 
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'about.html'

class SubmissionView(LoginRequiredMixin, ListView):
    model = DataSubmission
    template_name = 'submission.html'
    login_url = 'login'

