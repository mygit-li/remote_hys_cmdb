# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-09 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hys_operation', '0021_auto_20170828_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapaperstore',
            name='is_expired',
            field=models.CharField(default='未过期', max_length=20, verbose_name='是否已过期'),
        ),
    ]
