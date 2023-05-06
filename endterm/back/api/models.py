from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

class CreditCard(models.Model):
    number = models.CharField(max_length=16)
    expirationDate = models.DateField()
    CVC = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credit_cards')

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')
