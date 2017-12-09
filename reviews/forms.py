import os
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import get_available_image_extensions


class ClearableMultiFileInput(forms.ClearableFileInput):

	def value_from_datadict(self, data, files, name):
		print('-----------files.getlist(name))', files.getlist(name))
		return files.getlist(name)


class MultiFileExtensionValidator(validators.FileExtensionValidator):
	def __call__(self, value):
		for item in value:
			extension = os.path.splitext(item.name)[1][1:].lower()
			if self.allowed_extensions is not None and extension not in self.allowed_extensions:
				raise ValidationError(
					self.message,
					code=self.code,
					params={
						'extension': extension,
						'allowed_extensions': ', '.join(self.allowed_extensions)
					}
				)


validate_multi_image_file_extension = MultiFileExtensionValidator(
	allowed_extensions=get_available_image_extensions(),
)


class MultiImageField(forms.ImageField):
	default_validators = [validate_multi_image_file_extension]

	def to_python(self, data):
		print('22222222 entered to_python in MultiImageField 222222222222')
		data_list = []
		for chunk in data:
			print('--*chunk*--', chunk)
			f = super(MultiImageField, self).to_python(chunk)
			data_list.append(f)
		print('--*data_list*--', data_list)
		return data_list


class AddReviewForm(forms.Form):
	name = forms.CharField(label='Ваше имя')
	description = forms.CharField(label='Текст отзыва', widget=forms.Textarea)
	images = MultiImageField(required=False, widget=ClearableMultiFileInput(attrs={'multiple': True}))
	is_haircut = forms.BooleanField(label='Стрижка', required=False)
	is_shave = forms.BooleanField(label='Бритье', required=False)
	is_moustache = forms.BooleanField(label='Усы', required=False)



