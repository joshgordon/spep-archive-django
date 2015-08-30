# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0005_auto_20150829_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sermon',
            name='pastor',
            field=models.ForeignKey(to='archive.Pastor', null=True),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='series',
            field=models.ForeignKey(to='archive.Series', null=True),
        ),
    ]
