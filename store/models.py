from django.db import models
from users.models import CustomUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    product_name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    

class Store(models.Model):
    name = models.CharField(max_length= 255, default='null')
    location = models.CharField(max_length=225, default='null')
    
    def __str__(self):
        return str(self.name)