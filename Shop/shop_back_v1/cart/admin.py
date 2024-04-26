from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'items',)
    search_fields = ('user',)

@admin.register(CartItem)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sneakers', 'quantity',)