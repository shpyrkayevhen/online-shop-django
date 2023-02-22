from django.core.validators import MinValueValidator
from django.db import models

from category.models import Category


class Product(models.Model):
    '''Product db model.'''
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=252, unique=True)
    slug = models.SlugField(max_length=252, unique=True)
    description = models.TextField(max_length=252, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self: str) -> str:
        '''Product string representation.'''
        return self.product_name
        