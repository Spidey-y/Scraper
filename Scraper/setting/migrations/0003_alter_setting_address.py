# Generated by Django 4.1.4 on 2023-01-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0002_setting_delete_aboutus_delete_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='address',
            field=models.CharField(help_text='address (google map link)', max_length=255),
        ),
    ]
