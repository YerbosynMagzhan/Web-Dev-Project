from django.db import models
from django.contrib.auth.models import User
from sneakers.models import Sneakers
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def to_json(self):
        return {
            'id': self.id,
            'user': self.user.username,
           'sneakers': self.sneakers.name,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    def __str__(self):
        return f"ID: {self.id}, User: {self.user}, Sneakers: {self.sneakers}, Rating: {self.rating}, Comment: {self.comment}, Created at: {self.created_at}, Updated at: {self.updated_at}"
