from django.core.validators import MinValueValidator
from django.db import models

from store.models import Product


class Cart(models.Model):
    '''Cart db model.'''
    cart_id = models.CharField(max_length=252, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        '''Cart string representation.'''
        return self.cart_id


class CartItem(models.Model):
    '''CartItem db model.'''
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        '''CartItem string representation.'''
        return self.product