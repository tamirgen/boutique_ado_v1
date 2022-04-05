from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmim(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmim(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmim)
admin.site.register(Category, CategoryAdmim)
