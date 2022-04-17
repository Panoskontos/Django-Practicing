from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class MyBasket(models.Model):
    name = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MyBasket_Product(models.Model):
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
    basket = models.ForeignKey(MyBasket, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.basket.user.username} + {self.product.name}'
