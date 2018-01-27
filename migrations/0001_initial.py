# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('genres', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('fmt', models.CharField(max_length=20)),
                ('length', models.PositiveIntegerField()),
                ('url', models.URLField()),
                ('img', models.URLField()),
            ],
        ),
    ]
