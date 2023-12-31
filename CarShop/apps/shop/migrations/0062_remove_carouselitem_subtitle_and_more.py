# Generated by Django 4.2.1 on 2023-09-25 01:15

import apps.core.model_tools.integer_range_field
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0061_alter_buy_card_num_alter_buy_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carouselitem',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='carouselitem',
            name='title',
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=apps.core.model_tools.integer_range_field.IntegerRangeField(max_value=None, min_value=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
