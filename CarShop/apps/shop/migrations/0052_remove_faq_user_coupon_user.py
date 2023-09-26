# Generated by Django 4.2.1 on 2023-09-11 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0051_remove_profile_coupon_faq_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='user',
        ),
        migrations.AddField(
            model_name='coupon',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]