# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0027_auto_20150512_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetline',
            name='quote',
            field=models.FileField(null=True, upload_to=b'quotes', blank=True),
            preserve_default=True,
        ),
    ]
