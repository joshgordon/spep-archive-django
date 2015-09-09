# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0011_auto_20150909_0054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sermon',
            options={'ordering': ['-pub_date', 'sequence_num']},
        ),
    ]
