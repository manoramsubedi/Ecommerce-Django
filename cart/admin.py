from django.contrib import admin
from .models import Cart, CartItems


class CartAdmin(admin.ModelAdmin):
    list_display=('cart_id', 'date_added')
admin.site.register(Cart, CartAdmin)

class CartItemsAdmin(admin.ModelAdmin):
    pass
    list_display=('product', 'cart', 'quantity', 'is_active')
admin.site.register(CartItems, CartItemsAdmin)
