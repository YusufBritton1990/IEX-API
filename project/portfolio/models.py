from django.db import models
from user.models import Account
from django.utils import timezone

# Create your models here.
class StockPurchases(models.Model):
    acct_id = models.ForeignKey(Account,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    trans = models.CharField(max_length=5)
    ticker = models.CharField(max_length=5)
    qty = models.IntegerField()
    stock_value = models.FloatField()

    def stock_multiplier(self):
        "Multiples quantity by stock value."
        return qty * stock_value
    cash_effect = property(stock_multiplier)

    def __str__(self):
        return self.acct_id

class StockQuantity(models.Model):
    acct_id = models.ForeignKey(Account,on_delete=models.CASCADE)
    ticker = models.CharField(max_length=5)
    qty = models.IntegerField()

    def __str__(self):
        return self.acct_id
