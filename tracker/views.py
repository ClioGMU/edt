from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Submission, Sensor

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

    def form_valid(self, form):
        form.instance.institution = self.request.user.institution
        if form.is_valid():
            response = super().form_valid(form)
            form.instance = self.object
            form.save()
            return response
        else:
            return super().form_invalid(form)  

class SubmissionDeleteView(LoginRequiredMixin, DeleteView):
    model = Submission
    template_name = 'submission_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

class SensorListView(LoginRequiredMixin, ListView):
    model = Sensor
    template_name = 'sensor_list.html'
    login_url = 'login'
    def get_queryset(self):
        return Sensor.objects.all().filter(institution=self.request.user.institution)

class SensorDetailView(LoginRequiredMixin, DetailView):
    model = Sensor
    template_name = 'sensor_detail.html'
    login_url = 'login'

class SensorCreateView(LoginRequiredMixin, CreateView):
    model = Sensor
    template_name = 'sensor_new.html'
    fields = ['name', 'room', 'sensortype' ]
    login_url = 'login'    

    def form_valid(self, form):
        form.instance.institution = self.request.user.institution
        if form.is_valid():
            response = super().form_valid(form)
            form.instance = self.object
            form.save()
            return response
        else:
            return super().form_invalid(form)

class SensorUpdateView(LoginRequiredMixin, UpdateView):
    model = Sensor
    template_name = 'sensor_edit.html'
    fields = ['name', 'room', 'sensortype' ]
    login_url = 'login'    

class SensorDeleteView(LoginRequiredMixin, DeleteView):
    model = Sensor
    template_name = 'sensor_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'    