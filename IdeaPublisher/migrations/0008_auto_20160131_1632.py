# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IdeaPublisher', '0007_auto_20160124_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='titulo',
            field=models.CharField(verbose_name='Title', max_length=128, unique=True),
            preserve_default=True,
        ),
    ]
