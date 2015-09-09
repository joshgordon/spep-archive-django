# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0008_auto_20150829_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sermon',
            name='url',
            field=models.CharField(max_length=1024),
        ),
    ]
