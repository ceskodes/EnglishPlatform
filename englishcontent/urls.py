"""
URL configuration for englishplatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('A1/', views.A1GrammarView.as_view(), name='A1_view'),
    path('A2/', views.A2GrammarView.as_view(), name='A2_view'),
    path('B1/', views.B1GrammarView.as_view(), name='B1_view'),
    path('B2/', views.B2GrammarView.as_view(), name='B2_view'),
    path('C1/', views.C1GrammarView.as_view(), name='C1_view'),
    path('C2/', views.C2GrammarView.as_view(), name='C2_view')
]