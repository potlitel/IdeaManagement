# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IdeaPublisher', '0010_idea_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='project',
            field=models.CharField(blank=True, verbose_name='Project', max_length=2555, null=True),
            preserve_default=True,
        ),
    ]
