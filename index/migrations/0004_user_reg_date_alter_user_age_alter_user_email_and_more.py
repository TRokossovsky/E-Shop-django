# Generated by Django 4.2.1 on 2023-06-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_user_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reg_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]