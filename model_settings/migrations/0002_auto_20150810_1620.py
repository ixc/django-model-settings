# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boolean',
            name='value',
            field=models.BooleanField(default=False),
        ),
    ]
