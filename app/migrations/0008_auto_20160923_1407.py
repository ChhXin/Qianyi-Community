# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160923_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_sex',
            field=models.CharField(max_length=15, verbose_name='鎬у埆'),
        ),
    ]
