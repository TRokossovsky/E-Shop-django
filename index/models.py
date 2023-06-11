from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, IntegerField, CharField


class UserManager(BaseUserManager):
    def create_user(self, username, password, email, phone_number, age):
        user = self.model(
            username=username,
            password=password,
            email=email,
            number=phone_number,
            age=age
        )
        user.save()
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=50)
    password = CharField(max_length=400)
    email = EmailField(max_length=60, unique=True)
    phone_number = CharField(max_length=20, unique=True)
    age = IntegerField()
    reg_date = models.DateField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number', 'email', 'age', 'password']


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_desc = models.TextField(max_length=9999)
    product_price = models.FloatField()
    product_image = models.ImageField(default='../static/images/default_image.jpg', upload_to='images/')
