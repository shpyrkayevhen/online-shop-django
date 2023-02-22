from django.shortcuts import render


def cart(request):
    
    context = {}

    return render(request, 'store/cart.html', context)
