from django.contrib import admin

from sneakers.models import Sneakers, Category

@admin.register(Sneakers)
class SneakersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category')
    search_fields = ('name', )
    list_filter = ('price', 'category')
    # list_editable = ('price',)
    # list_per_page = 10
    # ordering = ('price',)
    # date_hierarchy = 'created_at'
    # readonly_fields = ('created_at', 'updated_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
