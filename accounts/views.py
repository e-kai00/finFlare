from django.shortcuts import render
from .models import UserAccountPortfolio, StockBalance
from decimal import Decimal


def user_profile(request):
    return render(request, 'accounts/profile.html')
