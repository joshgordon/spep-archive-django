# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0010_auto_20150909_0053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sermon',
            options={'ordering': ['-pub_date']},
        ),
    ]
