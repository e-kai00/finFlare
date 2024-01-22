
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User


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


def profile(request):
    """
    Render profile.html view
    """
    return render(request, "about/profile.html")


@login_required
def profile_delete(request, pk):
    user = get_object_or_404(User, id=pk)

    if user == request.user:
        logout(request)
        user.delete()
        messages.warning(request, "Your account has been deleted")
        return redirect("home")
    else:
        messages.error(request, "You are not authorized to delete this account.")
        return redirect("home")

