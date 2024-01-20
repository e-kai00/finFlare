from django.urls import path, include
from . import views

urlpatterns = [
    path('markets/', views.stock_data, name='markets'),
    path('stock_data/<str:symbol>/', views.stock_data, name='stock_data'),
]
