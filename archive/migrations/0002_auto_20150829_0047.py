# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sermon',
            name='pub_date',
            field=models.DateField(verbose_name=b'Date Preached'),
        ),
    ]
