# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0065_auto_20150709_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetline',
            name='amount',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
