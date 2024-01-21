from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('terms_of_service/', views.terms_of_service_view, name='terms_of_service'),
]