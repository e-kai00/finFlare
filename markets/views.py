from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
import requests
from django.contrib import messages
from .models import UserAccountPortfolio, StockBalance, Transaction, Stock
from decimal import Decimal


####################################################
#### API serpapi view functions - Fetching Data ####
####################################################
def get_market_data(api_key, category, max_items=5):
    """
    Fetch market data using SerpApi for a specified category
    """
    base_url = "https://serpapi.com/search.json"
    category = 'us' if category == 'Stocks US' else category.lower()
    symbols = {
        'us': ['DJI:INDEXDJX', 'SPX:INDEXSP', 'COMP:INDEXNASDAQ', 'RUT:INDEXRUS', 'VIX:INDEXCBOE'],
        'crypto': ['BTC:USD', 'ETH:USD', 'ADA:USD', 'XRP:USD', 'DOGE:USD'],
        'currencies': ['EUR:USD', 'USD:JPY', 'GBP:USD', 'USD:CAD', 'AUD:USD'],
        'futures': ['YMW00:CBOT', 'ESW00:CME_EMINIS', 'NQW00:CME_EMINIS', 'GCW00:COMEX', 'CLW00:NYMEX'],
    }

    symbols_list = symbols.get(category, [])
    market_data_list = []

    for symbol in symbols_list:
        params = {
            'engine': 'google_finance',
            'q': symbol,
            'api_key': api_key
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        market_info_list = data.get('markets', {}).get(category.lower(), [])

        for market_info in market_info_list:
            market_data_list.append({
                'symbol': symbol.split(':')[0],
                'name': market_info.get('name', ''),
                'price': market_info.get('price', ''),
                'price_movement': {
                    'movement': market_info.get('price_movement', {}).get('movement', ''),
                    'percentage': market_info.get('price_movement', {}).get('percentage', 0),
                },
            })

        if len(market_info_list) >= max_items:
            break

    return market_data_list


def stock_data(request):
    """
    View function for displaying market data
    """
    api_key = settings.API_KEY
    categories = ['Stocks US', 'Crypto', 'Currencies', 'Futures']

    selected_category = 'Stocks US'  # Default category

    if request.method == 'POST':
        selected_category = request.POST.get('stockSelector', selected_category)

    combined_data = {
        selected_category: get_market_data(api_key, selected_category),
    }    

    return render(request, 'markets/markets.html', {'combined_data': combined_data, 'selected_category': selected_category, 'categories': categories })
###################################################
#### API serpapi view functions - ENDS HERE #######
###################################################


# View for stock,user

def trade_stock(request):
   
    if request.method == 'POST':

        user_profile = UserAccountPortfolio.objects.get(user=request.user)
        name = request.POST.get('name')
        quantity = int(request.POST.get('stockSelector'))
        price = Decimal(request.POST.get('price'))
        transaction_type = request.POST.get('transaction_type')

       # Check if enough balance 
        if transaction_type == 'BUY':
            total_cost = quantity * price
            if user_profile.balance < total_cost:
                messages.error(request, "Insufficient funds to complete the purchase.")
                return render(request, 'markets/markets.html')
       
        transaction = Transaction.objects.create(
            user_profile=user_profile,
            name=name,
            quantity=quantity,
            price=price,
            transaction_type=transaction_type,
        )

        # Update the user's account balance and update the buy position
        if transaction_type == 'BUY':
            user_profile.balance -= total_cost
            user_profile.save()

            # Find the matching buy position to update
            buy_position = StockBalance.objects.filter(
                user=user_profile,
                stock__symbol=name,
                is_buy_position=True,
            ).first()

            if buy_position is None:
    
                buy_position = StockBalance.objects.create(
                    user=user_profile,
                    stock=Stock.objects.get(symbol=name),
                    quantity=quantity,  
                    purchase_price=price,  
                    is_buy_position=True,
                )

            # Update the buy position quantity
            buy_position.quantity -= quantity
            buy_position.save()

            # Check if the entire buy position is closed
            if buy_position.quantity == 0:
                messages.success(request, f"You have successfully bought and sold {quantity} shares of {name}.")
            else:
                messages.success(request, f"You have partially sold {quantity} shares of {name}.")

        elif transaction_type == 'SELL':
            total_cost = quantity * price
            sell_position = StockBalance.objects.get(
                user_profile=user_profile,
                stock__symbol=name,
                is_buy_position=True,
            )

            if sell_position.quantity != quantity:
                messages.error(request, f"You can only sell the entire position, not a partial quantity.")
                return render(request, 'markets/markets.html')

            # Update user's balance and delete the buy position
            user_profile.balance += quantity * price
            user_profile.save()

            sell_position.delete()

            messages.success(request, f"You have successfully sold the entire position of {name}.")

        return render(request, 'markets/markets.html')

    return render(request, 'markets/markets.html')




def test_trade_stock(request):
    # Replace the following with realistic data for testing
    dummy_data = {
        'user': request.user,
        'name': 'AAPL',
        'quantity': 10,
        'price': 150.0,
        'transaction_type': 'BUY',
    }

    return render(request, 'markets/markets.html', dummy_data)




