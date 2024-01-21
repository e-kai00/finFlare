from django.contrib.auth.models import User
from django.db import models
from accounts.models import UserAccountPortfolio


class Stock(models.Model):
    """
    Saving specific stock values to DB (coming from API)
    """
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=4) 
    price_movement = models.CharField(max_length=10) 


class StockBalance(models.Model):
    """
    Current Balance and purschase of User (open positions)
    """
    user = models.ForeignKey(UserAccountPortfolio, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=4) 
    is_buy_position = models.BooleanField(default=True)


class Transaction(models.Model):
    """
    Allow keep a record of all transactions
    """
    user_profile = models.ForeignKey(UserAccountPortfolio, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=4, choices=[('BUY', 'Buy'), ('SELL', 'Sell')])
    symbol = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

