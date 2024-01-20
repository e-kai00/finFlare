from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('thank-you/', views.thank_you, name='thank-you'),
]