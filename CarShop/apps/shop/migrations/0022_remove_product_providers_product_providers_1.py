# Generated by Django 4.2.1 on 2023-08-08 18:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0021_alter_product_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='providers',
        ),
        migrations.AddField(
            model_name='product',
            name='providers_1',
            field=models.ManyToManyField(help_text='Select a provider for this product', to=settings.AUTH_USER_MODEL),
        ),
    ]
