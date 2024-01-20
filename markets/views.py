from django.shortcuts import render
from django.conf import settings
import requests


def stock_data(request):
    """
    View function to retrieve stock market data and render it in the template.

    This function queries the SerpApi Google Finance endpoint for stock market data
    based on a list of stock symbols. It limits the data to a maximum number of items
    defined by 'max_items' and renders the results in the 'markets/markets.html' template.

    Parameters:
    - request: Django HttpRequest object

    Returns:
    - HttpResponse: Rendered HTML response containing stock market data
    """

    api_key = settings.API_KEY
    base_url = "https://serpapi.com/search.json"

    stocks = ['DJI:INDEXDJX', 'SPX:INDEXSP', 'COMP:INDEXNASDAQ', 'RUT:INDEXRUS', 'VIX:INDEXCBOE']
    max_items = 5  # Max rending items

    stock_data_list = []

    for stock in stocks:
        params = {
            'engine': 'google_finance',
            'q': stock,
            'api_key': api_key
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        stock_info_list = data.get('markets', {}).get('us', [])

        for stock_info in stock_info_list:
            print(data)
            stock_data_list.append({
                'symbol': stock.split(':')[0],
                'name': stock_info.get('name', ''),
                'price': stock_info.get('price', ''),
                'price_movement': {
                    'movement': stock_info.get('price_movement', {}).get('movement', ''),
                    'percentage': stock_info.get('price_movement', {}).get('percentage', 0),
                },
            })
            
            # Check if we have reached the maximum number of items
            if len(stock_data_list) >= max_items:
                break

        # Check if we have reached the maximum number of items
        if len(stock_data_list) >= max_items:
            break

    return render(request, 'markets/markets.html', {'stock_data': stock_data_list})
