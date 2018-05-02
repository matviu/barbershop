# -*- coding: utf-8 -*-
from django.db import models


class Entry(models.Model):
    last_name = models.CharField(max_length=100, verbose_name=u'Фамилия')
    first_name = models.CharField(max_length=100, verbose_name=u'Имя')
    second_name = models.CharField(max_length=100, verbose_name=u'Отчество', blank=True)
    tel_number = models.CharField(max_length=100, verbose_name=u'Контактный телефон', blank=True)
    email = models.EmailField(max_length=100, verbose_name=u'Контактный e-mail')
    add_info = models.TextField(max_length=200, verbose_name=u'доп. информация')

    BEARD_MODELS = (
        ('admiral', u'адмирал'),
        ('woodchoper', u'лесоруб'),
        ('polar', u'полярник'),
        ('merchant', u'боярин'),
        ('elder', u'мудрец'),
    )

    beard_model = models.CharField(max_length=100, verbose_name=u'модель бороды',
                                   choices=BEARD_MODELS)

    is_beard_paint = models.BooleanField(default=False, verbose_name=u'Подкрасить бороду')
    is_beard_brush = models.BooleanField(default=False, verbose_name=u'Причесать бороду')
    is_remove_gray = models.BooleanField(default=False, verbose_name=u'Убрать седину')
    is_moustache_spin = models.BooleanField(default=False, verbose_name=u'Накрутить усы')
    is_trim = models.BooleanField(default=False, verbose_name=u'Подровнять виски')
    is_polish_head = models.BooleanField(default=False, verbose_name=u'отполировать лысину')

    date_added = models.DateTimeField(verbose_name=u'дата и время создания', auto_now_add=True)
    date_record = models.DateTimeField(verbose_name=u'дата и время записи')

    class Meta:
        verbose_name = u'запись на прием'
        verbose_name_plural = u'записи на прием'
        ordering = ['-date_record']

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.last_name + ' ' + self.first_name




