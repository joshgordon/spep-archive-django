# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pastor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('bio', models.TextField(blank=True)),
                ('picture', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('short_description', models.CharField(max_length=128)),
                ('long_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sermon_title', models.CharField(max_length=128)),
                ('verse', models.CharField(max_length=128)),
                ('pub_date', models.DateTimeField(verbose_name='Date Preached')),
                ('main_thought', models.CharField(blank=True, max_length=512)),
                ('challenge', models.CharField(blank=True, max_length=512)),
                ('url', models.URLField()),
                ('thumbnail', models.URLField(blank=True)),
                ('video', models.URLField(blank=True)),
                ('pastor', models.ForeignKey(to='archive.Pastor')),
                ('series', models.ForeignKey(to='archive.Series')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='sermon',
            name='type',
            field=models.ForeignKey(to='archive.Type'),
        ),
        migrations.AddField(
            model_name='featured',
            name='featured',
            field=models.ForeignKey(to='archive.Sermon'),
        ),
    ]
