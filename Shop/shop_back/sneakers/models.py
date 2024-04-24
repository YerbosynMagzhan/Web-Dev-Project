from django.db import models

class Sneakers(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'price' : self.price,
            'image_url' : self.image_url,
            'is_active' : self.is_active,
            'category_id' : self.category_id,
            'category_name' : self.category.name
        }
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=250)
    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name
        }
    def __str__(self):
        return self.name
