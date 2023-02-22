from django.db import models


class Category(models.Model):
    '''Category db model.'''
    category_name = models.CharField(max_length=252, unique=True)
    slug = models.SlugField(max_length=252, unique=True)
    description = models.TextField(max_length=252, blank=True)
    category_img = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self: str) -> str:
        '''Category string representation.'''
        return self.category_name
         