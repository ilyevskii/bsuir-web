# Generated by Django 4.2.1 on 2023-09-21 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0055_remove_coupon_user_profile_coupons'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carouselitem',
            old_name='uuid',
            new_name='image_key',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='uuid',
            new_name='image_key',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='uuid',
            new_name='image_key',
        ),
    ]
