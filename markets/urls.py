from django.urls import path, include
from . import views

urlpatterns = [
    path('markets/', views.stock_data, name='markets'),
    path('stock_data/<str:symbol>/', views.stock_data, name='stock_data'),
    path('trade/', views.trade_stock, name='trade_stock'),
    path('test_trade_stock/', views.test_trade_stock, name='test_trade_stock'),    
]
