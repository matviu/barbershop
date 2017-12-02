from django.db import models

class Photo(models.Model):
	image = models.ImageField(upload_to='photos')
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=250)

	is_haircut = models.BooleanField(default=False)
	is_shave = models.BooleanField(default=False)
	is_moustache = models.BooleanField(default=False)

	is_best_month_job = models.BooleanField(default=False)

	def __str__(self):
		return self.name