# Generated by Django 4.2.1 on 2023-06-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='index/default_image.jpg', upload_to='images/'),
        ),
    ]
