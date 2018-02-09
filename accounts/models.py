from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.conf import settings
import os
from PIL import Image
import math


class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	age = models.PositiveIntegerField(blank=True, null=True)
	avatar = models.ImageField(upload_to='avatars')

	class Meta:
		verbose_name = 'Аккаунт'
		verbose_name_plural = 'Аккаунты'

	def __str__(self):
		return self.user.username

	def base_resize(self, width, height, suffix='--resize', crop=True):
		full_path = settings.BASE_DIR + self.avatar.url
		image_url = os.path.dirname(self.avatar.url)
		image_name, image_ext = os.path.splitext(
			os.path.basename(full_path)
		)
		image_dir = os.path.dirname(full_path)

		resize_path = image_dir + '/' + image_name + suffix + image_ext
		resize_url = image_url + '/' + image_name + suffix + image_ext

		im = Image.open(full_path)
		width_ratio = width/im.size[0]
		height_ratio = height/im.size[1]
		ratio = max(width_ratio, height_ratio)
		size = (math.ceil(im.size[0]*ratio), math.ceil(im.size[1]*ratio))

		if crop:
			x = int(abs(size[0] - width)/2)
			y = int(abs(size[1] - height)/2)



			box = (x, y, size[0]-x, size[1]-y)
			#print('x, y', x, y)
			im = im.resize(size, Image.ANTIALIAS).crop(box)
		else:
			im = im.resize(size, Image.ANTIALIAS)

		# print('width, height**************************', width, height)
		# print('width_ratio, height_ratio', width_ratio, height_ratio)
		# print('ratio', ratio)
		# print('size', size)

		im.save(resize_path)

		return resize_url

	@property
	def resize_200x200(self):
		return self.base_resize(200, 200, '--avatar')



