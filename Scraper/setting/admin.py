from django.contrib import admin
from .models import Setting
# Register your models here.


class SettingsAdmin(admin.ModelAdmin):
    list_display = (
        'phone_number',
        'email',
        'address',
    )


admin.site.register(Setting, SettingsAdmin)
