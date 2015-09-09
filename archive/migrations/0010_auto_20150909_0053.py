# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0009_auto_20150909_0047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pastor',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='sermon',
            options={'ordering': ['sermon_title']},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ['name']},
        ),
    ]
