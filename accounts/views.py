# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import FormView, TemplateView

from .forms import (
    AccountsAuthenticationForm, AccountsRegistrationForm, AccountsChangeForm,
)
from .models import Account




class AccountsRegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = AccountsRegistrationForm
    success_url = '/accounts/profile/'

    def get(self, request, *args, **kwargs):
        form = AccountsRegistrationForm(request.user)
        if request.user.is_authenticated:
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form })

    def post(self, request, *args, **kwargs):
        form = AccountsRegistrationForm(request.user, request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            avatar = request.FILES.get('avatar')

            user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email)
            user.set_password(form.cleaned_data['password'])

            account = Account.objects.create(age=age, avatar=avatar, user=user)

            user.save()
            account.save()

            login(request, user)

            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form })



class AccountsLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = AccountsAuthenticationForm
    success_url = '/accounts/profile/'

    def get(self, request, *args, **kwargs ):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        else:
            form = self.get_form()
            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            print('entered form.is_valid')
            self.form_valid(form)
            return redirect(self.success_url)
        else:
            print('form not valid')
            self.form_invalid(form)
            return render(request, self.template_name, {'form': form })


class AccountsLogoutView(auth_views.LogoutView):
    template_name = 'accounts/logged_out.html'


class AccountsProfileView(TemplateView, LoginRequiredMixin):
    template_name = 'accounts/profile.html'
    success_url = '/accounts/profile/'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and hasattr(user, 'account'):
            form = AccountsChangeForm(
                initial = {
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'age': user.account.age,
                }
            )
            form_password = PasswordChangeForm(user=user)
            context = {
                'user': user,
                'form': form,
                'form_password': form_password,
            }

            return render(request, self.template_name, context)
        else:
            return redirect('/accounts/login/')


    def post(self, request, *args, **kwargs):
        user = request.user
        form = AccountsChangeForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.account.age = form.cleaned_data['age']
            user.email = form.cleaned_data['email']
            if request.FILES.get('avatar'):
                user.account.avatar = request.FILES.get('avatar')

            user.save()
            user.account.save()

            return redirect(self.success_url)
        else:
            context = {
                'user': user,
                'form': form,
            }
            return render(request, self.template_name, context)










