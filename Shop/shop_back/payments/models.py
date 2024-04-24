from django.db import models
from orders.models import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=250)
    payment_date = models.DateTimeField(auto_now_add=True)
    def to_json(self):
        return {
            'id' : self.id,
            'amount_paid' : self.amount_paid,
            'payment_method' : self.payment_method,
            'payment_date' : self.payment_date
        }
    def __str__(self):
        return str(self.id)
