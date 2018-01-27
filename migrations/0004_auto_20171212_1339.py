# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-12 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pymovieshelf', '0003_auto_20170517_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='production',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='movie',
            name='rated',
            field=models.CharField(choices=[('0', 'R'), ('1', 'PG-13'), ('2', 'GENERAL')], default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='movie',
            name='sn',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='fmt',
            field=models.CharField(choices=[('0', 'Blu-Ray'), ('1', 'Blu-Ray 3D'), ('2', 'DVD'), ('3', 'Blu-Ray 4K')], max_length=1),
        ),
    ]
