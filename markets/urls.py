from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_data, name='markets'),
    path('stock_data/<str:symbol>/', views.stock_data, name='stock_data'),
    path('trade/', views.trade_stock, name='trade_stock'),
<<<<<<< vc-finflare-branch
    path('thank-you/', views.thank_you, name='thank_you'),
]
=======
    path('thank-you/', views.thank_you, name='thank_you'),
]
>>>>>>> main
