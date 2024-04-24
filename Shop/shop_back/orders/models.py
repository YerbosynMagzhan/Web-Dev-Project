from django.db import models
from django.contrib.auth.models import User
from sneakers.models import Sneakers

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    def to_json(self):
        return {
            'id' : self.id,
            'user_id' : self.user_id,
            'user_name' : self.user.username,
           'sneakers_id' : self.sneakers_id,
           'sneakers_name' : self.sneakers.name,
           'sneakers_price' : self.sneakers.price,
            'quantity' : self.quantity,
            'total_price' : self.total_price,
            'date' : self.date
        }
    def __str__(self):
        return self.user.username + " " + self.sneakers.name + " " + str(self.quantity) + " " + str(self.total_price) + " " + str(self.date) 

