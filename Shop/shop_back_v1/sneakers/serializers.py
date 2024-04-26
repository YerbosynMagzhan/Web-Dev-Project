from rest_framework import serializers
from sneakers.models import Sneakers, Category

class SneakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sneakers
        fields = ['id', 'name', 'price', 'image_url' ,'description','is_active' ,'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
