# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('IdeaPublisher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=128, unique=True)),
                ('descripcion', models.CharField(max_length=255, unique=True)),
                ('fecha_adicion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(max_length=2, default='AV', choices=[('AV', 'Available'), ('Not_AV', 'Not available')])),
                ('comentario', models.ManyToManyField(blank=True, null=True, to='IdeaPublisher.Comentario')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('topico', models.ForeignKey(to='IdeaPublisher.Topico')),
            ],
            options={
                'verbose_name': 'Idea',
                'verbose_name_plural': 'Ideas',
                'ordering': ['titulo'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comentario',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentario',
            name='descripcion',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
