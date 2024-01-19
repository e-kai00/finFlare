from django.shortcuts import render

def markets(request):
    """
    Render markets.html view
    """
    return render(request, "markets/markets.html")