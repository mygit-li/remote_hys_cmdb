# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-27 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hys_operation', '0005_auto_20170527_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='machineinfo',
            name='os_mark',
            field=models.CharField(max_length=600, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='machineinfo',
            name='os_pwd',
            field=models.CharField(max_length=40, null=True, verbose_name='密码'),
        ),
        migrations.AddField(
            model_name='machineinfo',
            name='os_user',
            field=models.CharField(max_length=30, null=True, verbose_name='主机用户名'),
        ),
    ]