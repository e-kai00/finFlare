from django.shortcuts import render
from django.contrib import messages


def home_view(request):    
    return render(request, 'home/index.html')