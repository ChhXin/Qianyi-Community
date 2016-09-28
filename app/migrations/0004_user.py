# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=256, verbose_name='姓名')),
                ('user_password', models.CharField(max_length=16, verbose_name='密码')),
                ('user_email', models.CharField(max_length=256, verbose_name='邮箱')),
                ('user_sex', models.CharField(max_length=5, verbose_name='性别')),
                ('user_addr', models.TextField(verbose_name='简介')),
                ('user_birth', models.DateTimeField(verbose_name='出生年月')),
            ],
        ),
    ]
