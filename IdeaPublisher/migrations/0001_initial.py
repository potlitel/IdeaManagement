# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['descripcion'],
                'verbose_name_plural': 'Comentarios',
                'verbose_name': 'Comentario',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Topicos',
                'verbose_name': 'Topico',
            },
            bases=(models.Model,),
        ),
    ]
