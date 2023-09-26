# Generated by Django 4.2.1 on 2023-08-14 14:41

from django.db import migrations
import apps.core.media_tools


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=apps.core.model_tools.AvatarField(blank=True, default='profile_avatars/avatar_default.jpg', storage=apps.core.media_tools.OverwriteCodedStorage(), upload_to='profile_avatars'),
        ),
    ]