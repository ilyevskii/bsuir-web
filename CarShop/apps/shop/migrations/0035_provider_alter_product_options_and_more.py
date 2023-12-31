# Generated by Django 4.2.1 on 2023-08-25 20:01

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('shop', '0034_alter_buy_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
            ],
            options={
                'permissions': [('provide_product', 'Can provide Products')],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='providers',
            field=models.ManyToManyField(blank=True, help_text='Select a provider for this product', related_name='products', to='shop.provider'),
        ),
    ]
