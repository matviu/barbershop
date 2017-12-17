from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		exclude = ['date_added']
		widgets = {
			'last_name': forms.TextInput(attrs={
				'class': 'appointment__text-field text-field',
				'placeholder': 'Фамилия'
			}),
			'first_name': forms.TextInput(attrs={
				'class': 'appointment__text-field text-field',
				'placeholder': 'Имя'
			}),
			'second_name': forms.TextInput(attrs={
				'class': 'appointment__text-field text-field',
				'placeholder': 'Отчество'
			}),
			'tel_number': forms.TextInput(attrs={
				'class': 'appointment__text-field text-field',
				'placeholder': 'Контактный телефон'
			}),
			'email': forms.TextInput(attrs={
				'class': 'appointment__text-field text-field',
				'placeholder': 'Контактный email'
			}),
			'add_info': forms.Textarea(attrs={
				'class': 'text-field appointment__add-info',
				'placeholder': 'Допю информация для мастера'
			}),
			'beard_model': forms.RadioSelect(attrs={
				'class': 'invisible-radiobox'
			}),
			'is_beard_paint': forms.CheckboxInput(attrs={
				'class': 'invisible-checkbox'
			}),
			'is_beard_brush': forms.CheckboxInput(attrs={
				'class': 'invisible-checkbox'
			}),
			'is_remove_gray': forms.CheckboxInput(attrs={
				'class': 'invisible-checkbox'
			}),
			'is_moustache_spin': forms.CheckboxInput(attrs={
				'class': 'invisible-checkbox'
			}),
			'is_trim': forms.CheckboxInput(attrs={
				'class': 'invisible-checkbox'
			}),
			'is_polish_head': forms.CheckboxInput(attrs={
				'class': 'invisible-checkbox'
			}),
		}


