from django.db import models
from user.models import User
from django.conf import settings


class Categorie(models.Model):
    categorie_name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return self.categorie_name


class Product(models.Model):
    full_name = models.CharField(max_length=255, blank=False, null=False)
    photo = models.ImageField(upload_to=settings.MEDIA_URL[1:], blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, )
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
    date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', blank=False, null=False)
    products = models.ManyToManyField(Product,)
    
    def __str__(self):
        return f'{str(self.user)}, {self.status}'
