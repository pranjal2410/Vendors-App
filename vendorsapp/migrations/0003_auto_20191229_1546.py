# Generated by Django 2.2.3 on 2019-12-29 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendorsapp', '0002_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='email',
            new_name='E_mail',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='f_name',
            new_name='First_Name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='l_name',
            new_name='Last_Name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='password',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='ph_no',
            new_name='Phone_No',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='u_name',
            new_name='Username',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='v_no_products',
            new_name='No_of_Products',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='v_name',
            new_name='Vendor_Name',
        ),
    ]