from rest_framework import serializers
from orders.models import Order

from rest_framework import serializers
from .models import Order
from sneakers.models import Sneakers
from django.contrib.auth.models import User

class OrderSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    sneakers = serializers.PrimaryKeyRelatedField(queryset=Sneakers.objects.all())
    quantity = serializers.IntegerField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    def create(self, validated_data):
        user = validated_data['user']
        sneakers = validated_data['sneakers']
        quantity = validated_data['quantity']
        total_price = quantity * sneakers.price

        order = Order.objects.create(
            user=user,
            sneakesr=sneakers,
            quantity=quantity,
            total_price=total_price
        )
        return order

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.total_price = instance.quantity * instance.sneakers.price
        instance.save()
        return instance

