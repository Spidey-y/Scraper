from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
try:
    from rest_framework.authtoken.models import TokenProxy as DRFToken
except ImportError:
    from rest_framework.authtoken.models import Token as DRFToken


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'email', 'phone_number', 'address')
    list_display_links = ('id', 'last_name', 'first_name',)
    search_fields = ['id', 'last_name', 'first_name', 'email', 'phone_number', 'address']
    list_per_page = 100
        

admin.site.site_header = "Scraper admin panel"
admin.site.site_url = "/products/add-products"
admin.site.docsroot = "/swagger"
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.unregister(DRFToken)

