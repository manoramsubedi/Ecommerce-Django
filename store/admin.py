from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'category', 'modified_date', 'is_availiable')
    prepopulated_fileds = {'slug': ('product_name',)}
admin.site.register(Product)