# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=150, verbose_name='Название услуги')),
                ('head_clean', models.CharField(choices=[('0', '(с мытьем головы)'), ('1', '(без мытья)')], max_length=200)),
                ('Price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('special_offers', models.CharField(max_length=200, verbose_name='Акции')),
            ],
        ),
        migrations.AddField(
            model_name='priceitem',
            name='price_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price_list.PriceList'),
        ),
    ]
