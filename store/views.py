from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.
def store(request, slug=None):
    categories = None
    products = None

    if slug != None:
        categories = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=categories, is_availiable=True)
        product_count = products.count()

    # if there's no slug passed
    else:
        products = Product.objects.all().filter(is_availiable=True)
        product_count = products.count()

    context = {"products":products, "product_count":product_count}
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {'single_product':single_product}
    return render(request, 'store/product-detail.html', context)

