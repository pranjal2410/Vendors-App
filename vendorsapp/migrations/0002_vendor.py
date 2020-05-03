# Generated by Django 2.2.3 on 2019-12-21 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_name', models.CharField(max_length=100)),
                ('v_no_products', models.IntegerField(default=0)),
            ],
        ),
    ]