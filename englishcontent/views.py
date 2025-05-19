from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import EnglishContent
from django.http import Http404
from django.template.defaultfilters import slugify

# Content Views based on English Level
class A1GrammarView(LoginRequiredMixin, ListView):
    template_name = "A1.html"
    model = EnglishContent
    context_object_name = "contents"
    
    def get_queryset(self, queryset=None):
        return EnglishContent.objects.filter(level='A1')

# Dynamic content URL and view
def A1_dynamic_content_view(request, title_slug):
    template_name = f"A1Topics/{title_slug}.html"
    return render(request, template_name)

class A2GrammarView(LoginRequiredMixin, ListView):
    template_name = "A2.html"
    model = EnglishContent
    context_object_name = "contents"
    
    def get_queryset(self, queryset=None):
        return EnglishContent.objects.filter(level='A2')
    
class B1GrammarView(LoginRequiredMixin, ListView):
    template_name = "B1.html"
    model = EnglishContent
    context_object_name = "contents"
    
    def get_queryset(self, queryset=None):
        return EnglishContent.objects.filter(level='B1')
    
class B2GrammarView(LoginRequiredMixin, ListView):
    template_name = "B2.html"
    model = EnglishContent
    context_object_name = "contents"
    
    def get_queryset(self, queryset=None):
        return EnglishContent.objects.filter(level='B2')
    
class C1GrammarView(LoginRequiredMixin, ListView):
    template_name = "C1.html"
    model = EnglishContent
    context_object_name = "contents"
    
    def get_queryset(self, queryset=None):
        return EnglishContent.objects.filter(level='C1')
    
class C2GrammarView(LoginRequiredMixin, ListView):
    template_name = "C2.html"
    model = EnglishContent
    context_object_name = "contents"
    
    def get_queryset(self, queryset=None):
        return EnglishContent.objects.filter(level='C2')