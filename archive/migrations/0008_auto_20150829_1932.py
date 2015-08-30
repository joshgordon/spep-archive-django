# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0007_auto_20150829_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sermon',
            name='sequence_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
