from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Trader(models.Model):
    trader = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.trader.username


class Trade(models.Model):
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2)
