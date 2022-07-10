# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IdeaPublisher', '0005_auto_20151220_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='descripcion',
            field=models.CharField(max_length=2555, unique=True),
            preserve_default=True,
        ),
    ]
