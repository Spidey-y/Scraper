from django.db import models
from user.models import User
from django.conf import settings


class Categorie(models.Model):
    categorie_name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return self.categorie_name


class Product(models.Model):
    full_name = models.CharField(max_length=255, blank=False, null=False)
    photo = models.ImageField(upload_to="products/", blank=True, max_length=1000)
    price = models.DecimalField(max_digits=20, decimal_places=2, )
    original_link = models.CharField(max_length=1000, blank=False, null=False)
    original_store = models.CharField(max_length=255, blank=False, null=False)
    brand = models.CharField(max_length=255, blank=True)
    time_added = models.DateTimeField(auto_now=True)
    staff_pick = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    categorie = models.ManyToManyField(Categorie)

    def __str__(self):
        return self.full_name
    

class Order(models.Model):
    STATUS_CHOICES = (
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('pending', 'Pending'),
        ('on_the_way', 'On the way'),
        ('deleted', 'Deleted')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    full_name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.CharField(max_length=13, blank=False, null=False)
    description = models.TextField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', blank=False, null=False)
    products = models.ManyToManyField(Product,)
    
    def __str__(self):
        return f'Order by: {str(self.full_name)}, {self.status}'
