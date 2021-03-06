# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('content', models.TextField(max_length=500, verbose_name='содержание')),
                ('description', models.TextField(max_length=500, verbose_name='описание')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'фрагмент',
                'verbose_name_plural': 'фрагменты',
                'ordering': ['title'],
            },
        ),
    ]
