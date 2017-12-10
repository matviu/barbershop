import os
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import get_available_image_extensions


class ClearableMultiFileInput(forms.ClearableFileInput):
	# override widget method in order to get all files from ImageField
	def value_from_datadict(self, data, files, name):
		if files:
			return files.getlist(name)
		else:
			return []


class MultiFileExtensionValidator(validators.FileExtensionValidator):
	def __call__(self, value):
		# iterate and validate each file, instead of validating list
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
		data_list = []
		# iterate and passed through every file instead of list
		for item in data:
			f = super(MultiImageField, self).to_python(item)
			data_list.append(f)
		return data_list


class AddReviewForm(forms.Form):
	name = forms.CharField(label='Ваше имя')
	description = forms.CharField(label='Текст отзыва', widget=forms.Textarea)
	images = MultiImageField(required=False, widget=ClearableMultiFileInput(attrs={'multiple': True}))
	is_haircut = forms.BooleanField(label='Стрижка', required=False)
	is_shave = forms.BooleanField(label='Бритье', required=False)
	is_moustache = forms.BooleanField(label='Усы', required=False)
