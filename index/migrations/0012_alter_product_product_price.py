# Generated by Django 4.2.1 on 2023-06-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(),
        ),
    ]
