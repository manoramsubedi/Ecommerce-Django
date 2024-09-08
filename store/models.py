from django.db import models
from category.models import Category

from django.urls import reverse

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

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

variation_category_choice = (
    ('color','color'),
    ('size', 'size'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product}"


