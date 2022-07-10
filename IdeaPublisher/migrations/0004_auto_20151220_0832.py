# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IdeaPublisher', '0003_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='comentario',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
