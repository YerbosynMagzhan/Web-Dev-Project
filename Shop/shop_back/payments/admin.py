from django.contrib import admin
from payments.models import Payment

@admin.register(Payment)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'amount_paid', 'payment_method', 'payment_date')