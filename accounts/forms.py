# -*- coding: utf-8 -*-
from django.contrib.auth import forms as auth_forms, password_validation
from django import forms
from django.forms import widgets

from django.utils.translation import ugettext, ugettext_lazy as _


class AccountsRegistrationForm(forms.Form):
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(AccountsRegistrationForm, self).__init__(*args, **kwargs)

    username = forms.CharField()
    password = forms.CharField(widget=widgets.PasswordInput())
    password2 = forms.CharField(widget=widgets.PasswordInput())
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField()

    age = forms.IntegerField(required=False)
    avatar = forms.ImageField(required=False)

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.user.username = self.cleaned_data.get('username')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.user)
        return password2


class AccountsChangeForm(forms.Form):
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(AccountsChangeForm, self).__init__(*args, **kwargs)


    username = forms.CharField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField()

    age = forms.IntegerField(required=False)
    avatar = forms.ImageField(required=False)


class AccountsAuthenticationForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        max_length=254,
        widget=widgets.TextInput(attrs={
            'autofocus': True,
            'class': 'text-field login-popup__login-field',
            'placeholder': 'Логин',
        }),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'text-field login-popup__password-field',
            'placeholder': 'Пароль'
        }),
    )

    remember = forms.BooleanField(
        widget=widgets.CheckboxInput(attrs={
            'class': 'login-popup__ibvisible-checkbox'
        }),
        required=False,
    )
