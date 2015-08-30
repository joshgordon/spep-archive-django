# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0006_auto_20150829_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured',
            name='featured',
            field=models.OneToOneField(to='archive.Sermon'),
        ),
    ]
