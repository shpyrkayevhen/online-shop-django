from django.shortcuts import render, get_object_or_404

from category.models import Category
from store.models import Product


def store(request, category_slug=None):
    '''Render all products or by category.'''

    category = None
    products = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True).all()
        products_count = products.count()
    
    else:
        products = Product.objects.filter(is_available=True).all()
        products_count = products.count()
    
    context = {
        'products': products, 
        'products_count': products_count
    }
    
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    '''Render single product detail.'''
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    
    context = {'product': product}
    
    return render(request, 'store/product_detail.html', context)