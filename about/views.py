from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About
from .forms import CollaborateForm
from django.contrib import messages


def about_view(request):

    about = get_object_or_404(About, pk=1)  

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
