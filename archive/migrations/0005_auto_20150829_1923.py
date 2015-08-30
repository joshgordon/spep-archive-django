# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0004_auto_20150829_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sermon',
            name='pub_date',
            field=models.DateField(verbose_name='Date Preached', blank=True),
        ),
    ]
