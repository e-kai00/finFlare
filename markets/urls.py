from django.urls import path, include
from . import views

urlpatterns = [
    path('markets/', views.stockPicker, name='markets'),
]