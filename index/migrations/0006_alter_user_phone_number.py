# Generated by Django 4.2.1 on 2023-06-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]