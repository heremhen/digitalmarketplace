# Generated by Django 4.2.5 on 2023-11-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_store', '0005_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
