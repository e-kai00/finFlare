from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, 'error_pages/404.htm', status=404)

def handler500(request):
    """ Error Handler 500 - Internal Server Error """
    return render(request, "error_pages/404.html", status=500)