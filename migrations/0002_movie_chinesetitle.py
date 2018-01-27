# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pymovieshelf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='chinesetitle',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
    ]
