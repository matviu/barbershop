# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class PriceList(models.Model):
	title = models.CharField(verbose_name='Заголовок', max_length=100)
	version = models.BooleanField(verbose_name='Отображать на сайте', default=False)
	special_offers = models.CharField(verbose_name='Акции', max_length=200)

	class Meta:
		verbose_name = 'Прайс'
		verbose_name_plural = 'Прайсы'

	def __str__(self):
		return self.title

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		if self.version:
			try:
				tmp = PriceList.objects.get(version=True)
				if tmp != self:
					tmp.version = False
					tmp.save()
			except ObjectDoesNotExist:
				pass
		super(PriceList, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class PriceItem(models.Model):
	price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE)
	service = models.CharField(verbose_name='Название услуги', max_length=150)

	ADD_SERVICES = (
		('0', '(с мытьем головы)'),
		('1', '(без мытья)'),
	)

	head_clean = models.CharField(max_length=200, choices=ADD_SERVICES)
	Price = models.PositiveIntegerField()

	def __str__(self):
		return self.service


