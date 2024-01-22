from django.urls import path, include
from . import views

urlpatterns = [
    path('markets/', views.stock_data, name='markets'),
    path('stock_data/<str:symbol>/', views.stock_data, name='stock_data'),
    path('trade/', views.trade_stock, name='trade_stock'),
    path('update_balances/', views.update_balances, name='update_balances'),
    path('get_user_balance/', views.get_user_balance, name='get_user_balance'),
    path('get_stock_prices/', views.get_stock_prices, name='get_stock_prices'),
    path('get_user_stock_balances/', views.get_user_stock_balances, name='get_user_stock_balances'),
]