from django.shortcuts import render, redirect
from store.models import Product, Variation
from .models import Cart, CartItems

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    product_variation = []
    if request.method == "POST":
        for item in request.POST:
            key = item      # If color = black, color stored in key and black is stored in value
            value = request.POST[key]
            #print(key, value)

            try:
                variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                product_variation.append(variation)
            except:
                pass

        # color = request.POST['color']
        # size = request.POST['size']


    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItems.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItems.DoesNotExist:
        cart_item = CartItems.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()

    return redirect('cart')


def cart(request):
    try:
        total = 0
        quantity = 0
        tax_percent = 2
        cart_items = []

        cart = Cart.objects.get(cart_id=_cart_id(request)) # Retrives the cart
        cart_items = CartItems.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items: # Iterates over each item in cart
            total += cart_item.total # First item total = total, then adds the total with second item total
            quantity += cart_item.quantity

        tax = (tax_percent * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'tax_percent': tax_percent,
        'grand_total': grand_total,
    }
    return render(request, "store/cart.html", context)

def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItems.objects.get(product=product, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')

def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItems.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')