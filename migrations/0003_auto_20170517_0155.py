# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pymovieshelf', '0002_movie_chinesetitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='no', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
