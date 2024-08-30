from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=150)
    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to='photos/product')
    stock = models.IntegerField(null=True)
    is_availiable = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product_name
