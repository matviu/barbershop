# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20171202_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='is_best_month_job',
            field=models.BooleanField(default=False),
        ),
    ]