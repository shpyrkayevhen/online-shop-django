from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Category model representation and registration in Admin panel.'''
    list_display = ['category_name', 'slug']
    prepopulated_fields = {
        'slug': ['category_name']
    }
