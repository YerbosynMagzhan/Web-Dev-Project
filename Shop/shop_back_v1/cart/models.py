from django.db import models
from django.contrib.auth.models import User
from sneakers.models import Sneakers

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} x {self.sneaker.name} "
    
    def get_total_price(self):
        return self.quantity * self.sneakers.price

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem, blank=True)

    def total_cost(self):
        total = 0
        for item in self.items.all():
            total += item.get_total_price()
        return total