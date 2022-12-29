# Generated by Django 4.1.4 on 2022-12-27 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_name_categorie_categorie_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='categorie_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='parent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.categorie'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('accepted', 'Accepted'), ('rejected', 'Rejected'), ('pending', 'Pending'), ('on_the_way', 'On the way')], default='pending', max_length=20),
        ),
    ]
