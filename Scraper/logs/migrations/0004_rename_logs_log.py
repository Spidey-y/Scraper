# Generated by Django 4.1.4 on 2022-12-28 23:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logs', '0003_alter_logs_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Logs',
            new_name='Log',
        ),
    ]
