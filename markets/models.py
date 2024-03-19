from django.contrib.auth.models import User
from django.db import models
from accounts.models import UserAccountPortfolio


class Stock(models.Model):
    """
    Saving stock values to DB (coming from API)
    """
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=4) 
    price_movement = models.CharField(max_length=10) 


class Transaction(models.Model):
    """
    Allows to keep record of all transactions
    """
    user = models.ForeignKey(UserAccountPortfolio, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=4, choices=[('BUY', 'Buy'), ('SELL', 'Sell')])
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT) 
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)


class StockBalance(models.Model):
    """
    Current Balance and purschase of User (open positions)
    """
    user = models.ForeignKey(UserAccountPortfolio, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    is_buy_position = models.BooleanField(default=True)

    @property
    def current_price(self):
        """ retrieve current price from the associated Stock """
        return self.stock.price
    
    # to update this method later
    @property
    def calculate_stock_value(self):
        """ calculate current stock balance """
        return self.quantity * self.price.price
    
    @property
    def calculate_average_open_price(self):
        transactions = Transaction.objects.filter(user=self.user, stock=self.stock)
        total_invested = sum(trans.quantity * trans.price for trans in transactions)
        total_quantity = sum(trans.quantity for trans in transactions)
        return total_invested / total_quantity if total_quantity > 0 else 0

    @property
    def claculate_profit_loss(self):
        """ calculate profit or loss """
        average_open_price = self.calculate_average_open_price
        return (self.curren_price - average_open_price) * self.quantity
    


    



