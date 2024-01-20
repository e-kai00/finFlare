from django.shortcuts import render

# Create your views here.

def contact(request):
    """
    Render contact.html view
    """
    return render(request, "contact/contact.html")