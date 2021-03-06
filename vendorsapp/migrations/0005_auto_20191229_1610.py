# Generated by Django 2.2.3 on 2019-12-29 10:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorsapp', '0004_auto_20191229_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='Product_Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='Product_Price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='No_of_Products',
            field=models.PositiveIntegerField(default=0, verbose_name='No. of Products'),
        ),
    ]
