from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import OneToOneField
from django.shortcuts import redirect
from django.urls import reverse


class Vendor(models.Model):
    Vendor_Name = models.CharField(max_length=100, verbose_name='Vendor Name')
    No_of_Products = models.PositiveIntegerField(default=0, verbose_name='No. of Products')
    Product_Name = models.CharField(max_length=100, null=True)
    Product_Price = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, validators=[MinValueValidator(0.0)])


class Profile(models.Model):
    First_Name = models.CharField(max_length=100, verbose_name='First Name')
    Last_Name = models.CharField(max_length=100, verbose_name='Last Name')
    Phone_No = models.CharField(max_length=12, verbose_name='Phone No.')
    E_mail = models.CharField(max_length=100, verbose_name='E-mail')
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile')

    def __str__(self):
        return self.user.username
