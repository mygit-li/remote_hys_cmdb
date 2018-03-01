# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-09 01:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hys_operation', '0025_record_trouble_type_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='server_ip_id',
            field=models.ForeignKey(db_column='server_ip_id', on_delete=django.db.models.deletion.CASCADE, to='hys_operation.MachineInfo', verbose_name='服务器'),
        ),
        migrations.AlterField(
            model_name='record',
            name='trouble_type_id',
            field=models.ForeignKey(db_column='trouble_type_id', on_delete=django.db.models.deletion.CASCADE, to='hys_operation.PartType', verbose_name='故障类型'),
        ),
    ]