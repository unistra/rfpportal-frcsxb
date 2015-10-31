# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0080_auto_20151031_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='note',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
