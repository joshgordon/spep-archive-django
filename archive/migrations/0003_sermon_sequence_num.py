# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0002_auto_20150829_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='sermon',
            name='sequence_num',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=False,
        ),
    ]
