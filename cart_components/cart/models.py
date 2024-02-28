# cart/models.py

from django.db import models
from django.contrib.auth.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantity * self.price

