# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0024_auto_20150426_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetline',
            name='category',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
