# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-26 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'city',
                'verbose_name': '城市分布表',
                'verbose_name_plural': '城市分布表',
            },
        ),
        migrations.CreateModel(
            name='MachineGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'machine_group',
                'verbose_name': '主机属组表',
                'verbose_name_plural': '主机属组表',
            },
        ),
        migrations.CreateModel(
            name='MachineInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_model', models.CharField(max_length=40)),
                ('machine_ip', models.CharField(max_length=15, unique=True)),
                ('cache', models.CharField(max_length=12)),
                ('cpu', models.CharField(max_length=4)),
                ('hard_disk', models.CharField(max_length=20)),
                ('machine_os', models.CharField(max_length=40)),
                ('application', models.CharField(max_length=600)),
                ('status', models.CharField(choices=[('on', '正常'), ('off', '损坏')], max_length=8)),
            ],
            options={
                'db_table': 'machine_info',
                'verbose_name': '主机信息表',
                'verbose_name_plural': '主机信息表',
            },
        ),
        migrations.CreateModel(
            name='MachineRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_room_name', models.CharField(max_length=40)),
                ('city_belonged', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hys_operation.City', verbose_name='所属城市')),
            ],
            options={
                'db_table': 'machine_room',
                'verbose_name': '机房信息表',
                'verbose_name_plural': '机房信息表',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('go_time', models.CharField(max_length=20, null=True)),
                ('temperature', models.IntegerField()),
                ('humidity', models.IntegerField(null=True, verbose_name=11)),
                ('net', models.CharField(max_length=10)),
                ('server', models.CharField(max_length=100)),
                ('trouble', models.CharField(max_length=200)),
                ('mark', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'record',
                'verbose_name': '巡检记录表',
                'verbose_name_plural': '巡检记录表',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, unique=True)),
                ('pass_word', models.CharField(max_length=32)),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('user_mobile', models.IntegerField(max_length=11)),
            ],
            options={
                'db_table': 'user_info',
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
            },
        ),
        migrations.CreateModel(
            name='UserJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=40)),
                ('department', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'user_job',
                'verbose_name': '职位表',
                'verbose_name_plural': '职位表',
            },
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hys_operation.UserJob'),
        ),
        migrations.AddField(
            model_name='record',
            name='act_man',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hys_operation.UserInfo', verbose_name='巡检人'),
        ),
        migrations.AddField(
            model_name='record',
            name='machine_room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hys_operation.MachineRoom', verbose_name='所属机房'),
        ),
        migrations.AddField(
            model_name='machineinfo',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hys_operation.MachineRoom', verbose_name='所属机房'),
        ),
        migrations.AddField(
            model_name='machineinfo',
            name='machine_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hys_operation.MachineGroup', verbose_name='所属组'),
        ),
        migrations.AddField(
            model_name='machineinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hys_operation.UserInfo', verbose_name='负责人'),
        ),
    ]
