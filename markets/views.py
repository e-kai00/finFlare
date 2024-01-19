from django.shortcuts import render

def stockPicker(request):
    return render(request, "markets/markets.html")
