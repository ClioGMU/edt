from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Submission

class HomePageView(TemplateView): 
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'about.html'

class SubmissionListView(LoginRequiredMixin, ListView):
    model = Submission
    template_name = 'submission_list.html'
    login_url = 'login'

class SubmissionDetailView(LoginRequiredMixin, DetailView):
    model = Submission
    template_name = 'submission_detail.html'
    login_url = 'login'

class SubmissionCreateView(LoginRequiredMixin, CreateView):
    model = Submission
    template_name = 'submission_new.html'
    fields = ['sensor', 'upload']
    login_url = 'login'    

class SubmissionDeleteView(LoginRequiredMixin, DeleteView):
    model = Submission
    template_name = 'submission_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

