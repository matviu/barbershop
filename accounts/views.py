from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView

from .forms import AccountsAuthenticationForm, AccountsRegistrationForm
from .models import Account




class AccountsRegistrationView(FormView):
	template_name = 'accounts/registration.html'
	form_class = AccountsRegistrationForm
	success_url = '/accounts/login/'

	def post(self, request, *args, **kwargs):
		form = AccountsRegistrationForm(request.POST, request.FILES)

		if form.is_valid():
			username = form.cleaned_data['username']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			age = form.cleaned_data['age']
			avatar = request.FILES.get('avatar')


			user = User.objects.create(username=username, first_name=first_name, last_name=last_name)
			user.set_password(form.cleaned_data['password'])

			account = Account.objects.create(age=age, avatar=avatar, user=user)

			user.save()
			account.save()

			return redirect(self.success_url)
		else:
			return render(request, self.template_name, {'form': form })



class AccountsLoginView(auth_views.LoginView):
	template_name = 'accounts/login.html'
	form_class = AccountsAuthenticationForm
	#form_class = AuthenticationForm
	success_url = '/reviews/'

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







