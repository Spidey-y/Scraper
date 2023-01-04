import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {'categorie__categorie_name': ['exact', 'in'],
                  'brand': ['exact', 'in'],
                  'original_store': ['exact', 'in'],
                  'id': ['exact'],
                  'price': ['lte', 'gte'],
                  'staff_pick': ['exact']}
