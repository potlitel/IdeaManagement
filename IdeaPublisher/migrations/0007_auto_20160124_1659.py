# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IdeaPublisher', '0006_auto_20160124_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='estado',
            field=models.CharField(max_length=6, default='AV', choices=[('AV', 'Available'), ('Not_AV', 'Not available')]),
            preserve_default=True,
        ),
    ]
