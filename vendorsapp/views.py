from django.contrib import auth
from django.contrib.auth import authenticate
from django.core import mail
from django.http import request, HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Profile, Vendor
from django import forms
from . import forms as f1
from django.db import models
from django.conf import settings


class MainView(View):
    template_name = 'Main.html'

    def get(self, request):
        return render(request, self.template_name)


class SignupView(View):
    form_class = f1.MyForm
    template_name = 'profile_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            try:
                user = User.objects.get(username=username)
                form = self.form_class(None)
                return render(request, self.template_name, {'form': form, 'msg': 'User already exists'})

            except User.DoesNotExist:
                obj = Profile()
                obj.f_name = form.cleaned_data['First_Name']
                obj.l_name = form.cleaned_data['Last_Name']
                obj.email = form.cleaned_data['E_mail']
                obj.ph_no = form.cleaned_data['Phone_No']
                obj.u_name = username
                obj.password = password
                obj.user = User.objects.create_user(username=username, password=password)
                auth.login(request, obj.user)
                mail.send_mail('Vendors Registration', 'Registered successfully!', settings.EMAIL_HOST_USER,
                               [obj.email,
                                'newalkarpranjal2410.pn@gmail.com'
                                ])
                obj.save()
            return redirect(reverse('home'))

        else:
            return redirect(reverse('Login'))


class LoginView(View):
    template_name = 'Login.html'
    form_class = f1.LoginForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        try:
            user1 = form.save(commit=False)
            u_name = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            user = authenticate(username=u_name, password=password)
            db = User.objects.all()
            for u in db:
                if user is not None and user == u:
                    auth.login(request, user)
                    return redirect(reverse('home'))
            else:
                form = self.form_class(None)
                return render(request, self.template_name, {'form': form, 'msg': 'Username of password is incorrect'})
        except User.DoesNotExist:
            return render(request, self.template_name, {'msg': 'User does not Exists'})


class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'vendors'

    def get_queryset(self):
        return Vendor.objects.all


class DetailsView(DetailView):
    model = Vendor
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class VendorView(View):
    template_name = 'vendor_form.html'
    form_class = f1.VendorForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.save()
            return redirect(reverse('home'))


class VendorUpdate(UpdateView):
    model = Vendor
    template_name = 'vendor_form.html'
    fields = ['Vendor_Name', 'No_of_Products', 'Product_Name', 'Product_Price']
    success_url = reverse_lazy('home')


class SearchView(View):
    model = Vendor

    def post(self, request):
        name = request.POST.get('search')
        db = Vendor.objects.all()
        for v in db:
            if name == v.Vendor_Name:
                return redirect(reverse('details', kwargs={'pk': v.pk}))
        return redirect(reverse('home'))


class LogoutView(View):
    def get(self, request):
        if request.user.is_active:
            auth.logout(request)
            return redirect(reverse('main'))

    def post(self, request, **kwargs):
        auth.logout(request)
        return redirect(reverse('deactivateProfile', kwargs=kwargs))


class ProfileView(View):
    model = Profile
    template_name = 'profile.html'

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        return render(request, self.template_name, {'profile': profile})


class VendorDelete(DeleteView):
    model = Vendor
    success_url = reverse_lazy('home')


class ProfileDelete(DeleteView):
    model = Profile
    model = User
    success_url = reverse_lazy('home')


class Search(View):
    def get(self, request):
        search_data = request.GET.get('search')
        data = {
            'exists': Vendor.objects.filter(Vendor_Name=search_data).exists()
        }
        return JsonResponse(data)
