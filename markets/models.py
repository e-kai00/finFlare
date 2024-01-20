from django.contrib.auth.models import User
from django.db import models
from accounts.models import UserAccountPortfolio


class Stock(models.Model):
    """
    Saving specific stock values to DB
    """
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    price_movement = models.CharField(max_length=10)


class StockBalance(models.Model):
    """
    Current Balance and purschase of User
    """
    user = models.ForeignKey(UserAccountPortfolio, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=4)
