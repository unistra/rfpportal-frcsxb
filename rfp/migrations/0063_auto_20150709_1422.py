# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0062_auto_20150709_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default=b'draft', max_length=255, choices=[(b'draft', b'Draft'), (b'submitted', b'Submitted'), (b'under_review', b'Under review'), (b'granted', b'Granted'), (b'not_granted', b'Not Granted')]),
            preserve_default=True,
        ),
    ]
