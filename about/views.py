
from django.shortcuts import render

def about(request):
    """
    Render about.html view
    """
    return render(request, "about/about.html")