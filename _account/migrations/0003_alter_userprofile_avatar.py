# Generated by Django 4.2.5 on 2023-11-16 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_account', '0002_remove_userprofile_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to='avatars/'),
        ),
    ]
