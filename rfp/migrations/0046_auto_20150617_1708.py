# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0045_auto_20150617_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default=b'pending', max_length=255, choices=[(b'pending', b'Pending'), (b'under_review', b'Under Review'), (b'granted', b'Granted'), (b'not_granted', b'Not Granted')]),
            preserve_default=True,
        ),
    ]
