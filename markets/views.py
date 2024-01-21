from django.shortcuts import render
from django.conf import settings
import requests


def get_market_data(api_key, category, max_items=5):
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
        print(data)
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
    api_key = settings.API_KEY
    categories = ['Stocks US', 'Crypto', 'Currencies', 'Futures']

    if request.method == 'POST':
        selected_category = request.POST.get('stockSelector')
        if selected_category in categories:
            combined_data = {
                selected_category: get_market_data(api_key, selected_category),
            }
            print(combined_data)
        else:
            combined_data = {}  # handle invalid category selection

        return render(request, 'markets/markets.html', {'combined_data': combined_data, 'selected_category': selected_category, 'categories': categories})

    return render(request, 'markets/markets.html', {'categories': categories})
