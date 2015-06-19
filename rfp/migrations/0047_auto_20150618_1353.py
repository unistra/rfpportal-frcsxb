# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0046_auto_20150617_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='status',
            field=models.CharField(default=b'pending', max_length=255, choices=[(b'pending', b'pending'), (b'refused', b'refused'), (b'accepted', b'accepted'), (b'completed', b'completed')]),
            preserve_default=True,
        ),
    ]
