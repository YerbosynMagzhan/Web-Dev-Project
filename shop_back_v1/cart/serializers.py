from rest_framework import serializers
from cart.models import Cart, CartItem
from sneakers.serializers import SneakersSerializer

class CartItemSerializer(serializers.ModelSerializer):
    sneakers = SneakersSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'sneakers', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'