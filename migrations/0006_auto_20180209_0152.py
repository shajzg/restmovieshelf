# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-09 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pymovieshelf', '0005_auto_20171227_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.URLField(default=''),
        ),
    ]
