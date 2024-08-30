from django.shortcuts import render
from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_availiable=True)
    context = {"products":products}

    return render(request, 'nepkart/home.html', context)