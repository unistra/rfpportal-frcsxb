# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0074_auto_20150715_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfpcampaign',
            name='template',
            field=models.FileField(null=True, upload_to=b'rfp_templates', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proposedreviewer',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'ADMIN_PROPOSED', b'Proposed by Admin'), (b'USER_PROPOSED', b'Proposed by User'), (b'USER_EXCLUDED', b'Excluded Reviewer'), (b'BOARD_SUGGESTED', b'Proposed by Board Member')]),
            preserve_default=True,
        ),
    ]
