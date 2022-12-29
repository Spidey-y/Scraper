from django.contrib import admin
from .models import Log


class LogsAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    search_fields = ['user__first_name', 'user__last_name', 'timestamp']
    list_per_page = 100


admin.site.register(Log, LogsAdmin)
