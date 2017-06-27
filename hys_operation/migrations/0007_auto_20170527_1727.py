# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-27 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hys_operation', '0006_auto_20170527_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='mark',
            field=models.CharField(max_length=200, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='record',
            name='net',
            field=models.CharField(max_length=200, verbose_name='网络设备'),
        ),
        migrations.AlterField(
            model_name='record',
            name='server',
            field=models.CharField(max_length=200, verbose_name='服务器'),
        ),
    ]