from django.shortcuts import render
from django.contrib import messages


def home_view(request):
    # messages.success(request, 'This is a test success message.')
    messages.warning(request, 'This is a warning message.')
    messages.error(request, 'This is an error message.')
    messages.info(request, 'This is an info message.')
    return render(request, 'home/index.html')