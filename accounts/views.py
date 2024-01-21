from django.shortcuts import render
from .models import UserAccountPortfolio, StockBalance
from decimal import Decimal


def user_profile(request):
    return render(request, 'accounts/profile.html')


def portfolio(request):    
    user = request.user
    
    try:
        user_portfolio = UserAccountPortfolio.objects.get(user=user)
        balance = user_portfolio.balance
        
        open_positions = StockBalance.objects.filter(user=user, is_buy_position=True)
        stock_names = []
        stock_quantities = []

        for position in open_positions:
            stock_names.append(position.stock.name)
            stock_quantities.append(position.quantity)

        context = {
            'balance': balance,
            'stock_names': stock_names,
            'stock_quantities': stock_quantities,
        }

    except UserAccountPortfolio.DoesNotExist:
        
        context = {
            'balance': 10000.0,
            'stock_names': [],
            'stock_quantities': [],
        }

    return render(request, 'my_wallet.html', context)