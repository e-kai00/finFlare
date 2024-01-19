from django.urls import path
from .views import accounts_view

urlpatterns = [
    path('accounts/', views.user_profile, name='user_profile'),
]