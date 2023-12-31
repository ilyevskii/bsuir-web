# Generated by Django 4.2.1 on 2023-08-25 20:19

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('shop', '0035_provider_alter_product_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Provider',
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('provide_product', 'Can provide Products')],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='Product',
            name='providers',
            field=models.ManyToManyField(blank=True, help_text='Select a provider for this product', related_name='products', to='shop.provider'),
        ),
    ]
