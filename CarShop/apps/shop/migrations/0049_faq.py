# Generated by Django 4.2.1 on 2023-09-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0048_alter_review_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=64)),
                ('content', models.TextField()),
            ],
        ),
    ]
