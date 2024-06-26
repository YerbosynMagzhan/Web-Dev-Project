from django.contrib import admin
from orders.models import Order

@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    search_fields = ('user', 'sneakers')
    