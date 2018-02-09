# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='beard_model',
            field=models.CharField(choices=[('admiral', 'адмирал'), ('woodchoper', 'лесоруб'), ('polar', 'полярник'), ('merchant', 'боярин'), ('elder', 'мудрец')], max_length=100, verbose_name='модель бороды'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='second_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='tel_number',
            field=models.CharField(blank=True, max_length=100, verbose_name='Контактный телефон'),
        ),
    ]