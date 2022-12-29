from django.contrib import admin
from .models import Product, Order, Categorie


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name',
                    'price',
                    'original_store',
                    'brand',
                    'time_added',
                    'staff_pick',)
    search_fields = ('full_name', 'original_store', 'brand')
    list_filter = ('categorie__categorie_name', 'brand', 'original_store')
    list_per_page = 100


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',
                    'date',
                    'status',)
    search_fields = ('user__last_name', 'user__first_name')
    list_filter = ('status', )
    ordering = ['-date']
    list_per_page = 100


class CateAdmin(admin.ModelAdmin):
    list_display = ('id', 'categorie_name',)
    search_fields = ('categorie_name',)
    list_per_page = 100


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Categorie, CateAdmin)
