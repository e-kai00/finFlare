
from django.shortcuts import render

def about(request):
    """
    Render about.html view
    """
    return render(request, "about/about.html")

def thank_you(request):
    """
    Render thank-you.html view
    """
    return render(request, "about/thank-you.html")