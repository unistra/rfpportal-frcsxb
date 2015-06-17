# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0044_auto_20150617_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfpcampaign',
            name='status',
            field=models.CharField(default=b'open', max_length=255, null=True, choices=[(b'open', b'Open, Call for proposal is open for submission.'), (b'under_review', b'Under review, reviews are being collected prior to board meeting.'), (b'closed', b'Closed, results have been communicated.')]),
            preserve_default=True,
        ),
    ]
