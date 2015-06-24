# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0055_auto_20150623_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposedreviewer',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'ADMIN_PROPOSED', b'Proposed by admin'), (b'USER_PROPOSED', b'Proposed by User'), (b'USER_EXCLUDED', b'Excluded Reviewer')]),
            preserve_default=True,
        ),
    ]
