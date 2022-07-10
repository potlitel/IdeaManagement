# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IdeaPublisher', '0009_auto_20160131_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='project',
            field=models.CharField(max_length=2555, null=True, verbose_name='Description of project', blank=True),
            preserve_default=True,
        ),
    ]
