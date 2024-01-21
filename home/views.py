from django.shortcuts import render
from django.contrib import messages


def home_view(request):    
    return render(request, 'home/index.html')


def privacy_view(request):    
    return render(request, 'home/privacy.html')


def terms_of_service_view(request):    
    return render(request, 'home/terms_of_service.html')
