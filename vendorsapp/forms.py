from django import forms
from django.forms import TextInput

from .models import Profile, Vendor
from django.contrib.auth.models import User


class MyForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['First_Name', 'Last_Name', 'Phone_No', 'E_mail', 'Username', 'Password']


class LoginForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['Username', 'Password']


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['Vendor_Name', 'No_of_Products', 'Product_Name', 'Product_Price']
