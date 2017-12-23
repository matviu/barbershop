from django.db import models

class Chunk(models.Model):
	title = models.CharField(max_length=100, verbose_name='название')
	content = models.TextField(max_length=500, verbose_name='содержание')
	description = models.TextField(max_length=500, verbose_name='описание')
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['title']
		verbose_name='фрагмент'
		verbose_name_plural = 'фрагменты'

	def __str__(self):
		return self.title



