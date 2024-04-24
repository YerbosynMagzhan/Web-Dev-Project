from django.contrib import admin
from reviews.models import Review

@admin.register(Review)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sneakers', 'rating', 'comment')
    search_fields = ('sneakers', 'user')
