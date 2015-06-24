# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0054_auto_20150622_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposedreviewer',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'ADMIN_PROPOSED', b'Proposed by admin'), (b'USER_PROPOSED', b'Proposed by User')]),
            preserve_default=True,
        ),
    ]
