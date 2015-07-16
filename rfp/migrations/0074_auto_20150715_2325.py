# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0073_auto_20150714_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='awarded_amount',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default=b'draft', max_length=255, choices=[(b'draft', b'Draft'), (b'submitted', b'Submitted'), (b'granted', b'Granted'), (b'not_granted', b'Not Granted')]),
            preserve_default=True,
        ),
    ]
