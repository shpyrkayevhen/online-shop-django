from django.shortcuts import render

from store.models import Product


def home(request):
    """Return home page with all products."""
    products = Product.objects.filter(is_available=True).all()
    context = {'products': products}

    return render(request, 'home.html', context)
