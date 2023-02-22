from django.contrib import admin

from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    '''Cart model registration and representation in Admin panel.'''
    pass


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    '''CartItem model registration and representation in Admin panel.'''
    pass
