from django.contrib.auth import forms as auth_forms
from django import forms
from django.forms import widgets

from django.utils.translation import ugettext, ugettext_lazy as _


class AccountsRegistrationForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=widgets.PasswordInput())
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)

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
