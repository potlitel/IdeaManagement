# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('IdeaPublisher', '0004_auto_20151220_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
    ]
