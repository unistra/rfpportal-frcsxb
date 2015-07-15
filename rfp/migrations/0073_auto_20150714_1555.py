# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0066_auto_20150709_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='note',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
