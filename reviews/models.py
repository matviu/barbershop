from django.db import models
from django.conf import settings
import os
import math
from PIL import Image

class Review(models.Model):
	name = models.CharField(verbose_name='Имя', max_length=100)
	description = models.TextField(verbose_name='Описание', max_length=250)
	date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
	date_updated = models.DateTimeField(verbose_name='дата обновления', auto_now=True)

	is_haircut = models.BooleanField(verbose_name='стрижка', default=False)
	is_shave = models.BooleanField(verbose_name='бритье', default=False)
	is_moustache = models.BooleanField(verbose_name='усы', default=False)
	is_best_month_job = models.BooleanField(verbose_name='работа месяца', default=False)

	class Meta:
		verbose_name = 'Отзыв'
		verbose_name_plural = 'Отзывы'
		ordering = ['date_created']

	def __str__(self):
		return self.name


class ReviewPhoto(models.Model):
	image = models.ImageField(verbose_name='фото', upload_to='reviews')
	is_main = models.BooleanField(verbose_name='главное фото', default=False)
	review = models.ForeignKey(Review, on_delete=models.CASCADE)

	def __str__(self):
		return self.image.path


	def base_resize(self, width, height, suffix='--resize', crop=True):
		full_path = settings.BASE_DIR + self.image.url
		image_url = os.path.dirname(self.image.url)
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
	def resize_480x480(self):
		return self.base_resize(480, 480, '--main')

	@property
	def resize_289x289(self):
		return self.base_resize(289, 289, '--secondary')
