# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IdeaPublisher', '0008_auto_20160131_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='descripcion',
            field=models.CharField(unique=True, max_length=2555, verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='idea',
            name='estado',
            field=models.CharField(max_length=6, choices=[('AV', 'Available'), ('Not_AV', 'Not available')], default='AV', verbose_name='State'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='idea',
            name='topico',
            field=models.ForeignKey(to='IdeaPublisher.Topico', verbose_name='Topic'),
            preserve_default=True,
        ),
    ]
