from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class LoggedHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home_logged.html'
    
    

