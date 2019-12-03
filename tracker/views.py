from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import DataSubmission 

class HomePageView(TemplateView): 
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'about.html'

class SubmissionListView(LoginRequiredMixin, ListView):
    model = DataSubmission
    template_name = 'submission_list.html'
    login_url = 'login'

class SubmissionDetailView(LoginRequiredMixin, DetailView):
    model = DataSubmission
    template_name = 'submisstion_detail.html'
    login_url = 'login'

