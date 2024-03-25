from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_data, name='markets'),
    path('stock_data/<str:symbol>/', views.stock_data, name='stock_data'),
    path('trade/', views.trade_stock, name='trade_stock'),
]
