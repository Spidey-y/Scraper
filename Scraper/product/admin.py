from django.contrib import admin
from .models import Product, Order, Categorie
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name',
                    'price',
                    'original_store',
                    'brand',
                    'time_added',
                    'staff_pick',)
    list_display_links = ('id', 'full_name',)
    search_fields = ('full_name', 'original_store', 'brand')
    list_filter = ('categorie__categorie_name', 'brand', 'original_store')
    list_per_page = 100
    readonly_fields =( 'categorie',)
    list_editable = ('staff_pick',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',
                    'date',
                    'status', )
    list_display_links = ('id', 'user', )
    search_fields = ('user__last_name', 'user__first_name')
    list_filter = ('status', )
    ordering = ['-date']
    readonly_fields = ( 'get_products', 'user')
    exclude = ('products',)
    list_per_page = 100
    @admin.display(
    description='Products',
    )
    def get_products(self, obj):
        tmp = obj.products.all()
        arr = []
        for i in tmp:
            arr.append([i.original_link, i.original_store, i.full_name])
        return format_html_join(
            mark_safe('<br>'),
            '<a href="{0}">({1})  {2}</a>',
            ((line[0],line[1],line[2]) for line in arr),
        )


class CateAdmin(admin.ModelAdmin):
    list_display = ('id', 'categorie_name',)
    list_display_links = ('id', 'categorie_name',)
    search_fields = ('categorie_name',)
    list_per_page = 100


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Categorie, CateAdmin)
