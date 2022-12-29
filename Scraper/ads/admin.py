from django.contrib import admin
from .models import Ad


class AdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',
                    'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'position')
    list_per_page = 100


admin.site.register(Ad, AdsAdmin)
