from django.shortcuts import render, redirect
from matplotlib.style import context
from .models import *
# Create your views here.


def home(request):
    product = Product.objects.all()

    #
    items = MyBasket_Product.objects.all()
    frequencies = {}
    total = 0
    for i in items:
        frequencies[i.product.name] = 0
    for i in items:
        total += i.product.price
        frequencies[i.product.name] += 1

    Basketitems = items.count()
    print(frequencies)

    context = {
        'product': product,
        'Basketitems': Basketitems,
        'total': total,
        'frequencies': frequencies,
    }

    return render(request, 'home.html', context)


def checkout(request):
    items = MyBasket_Product.objects.all()
    frequencies = {}
    total = 0
    for i in items:
        frequencies[i.product.name] = 0
    for i in items:
        total += i.product.price
        frequencies[i.product.name] += 1
    Basketitems = items.count()
    context = {
        'Basketitems': Basketitems,
        'total': total,
        'frequencies': frequencies,
    }
    return render(request, 'checkout.html', context)


def add_product_to_basket(request, product_id):
    product = Product.objects.get(name=product_id)
    basket = MyBasket.objects.get(user=request.user)
    new = MyBasket_Product(product=product, basket=basket)
    new.save()
    return redirect('home')


def remove_product_from_basket(request, product_id):
    product = Product.objects.get(name=product_id)
    basket = MyBasket.objects.get(user=request.user)
    new = MyBasket_Product.objects.filter(product=product, basket=basket)
    if new:
        new = new[0]
    new.delete()
    return redirect('home')
