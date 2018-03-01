# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-24 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hys_operation', '0046_auto_20180116_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='machineinfo',
            name='app_type',
            field=models.CharField(choices=[('WEB', 'WEB'), ('DB', 'DB')], default='WEB', max_length=8, verbose_name='应用类型'),
        ),
    ]