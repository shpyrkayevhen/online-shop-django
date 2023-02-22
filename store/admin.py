from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Product model representation and registration in Admin panel.'''
    list_display = ['product_name', 'price', 'stock', 'category', 'modified_date', 'is_available']
    prepopulated_fields = {
        'slug': ['product_name']
    }
