# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0003_sermon_sequence_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured',
            name='featured',
            field=models.ForeignKey(to='archive.Sermon', unique=True),
        ),
        migrations.AlterField(
            model_name='pastor',
            name='name',
            field=models.CharField(unique=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='series',
            name='long_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(unique=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='series',
            name='short_description',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
