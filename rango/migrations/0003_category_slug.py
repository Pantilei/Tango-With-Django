# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-11-12 09:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20181109_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2018, 11, 12, 9, 45, 35, 431717, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
