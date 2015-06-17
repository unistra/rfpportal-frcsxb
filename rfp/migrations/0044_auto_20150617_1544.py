# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0043_auto_20150615_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfpcampaign',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2015, 6, 17, 19, 44, 48, 873000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rfpcampaign',
            name='status',
            field=models.CharField(max_length=255, null=True, choices=[(b'open', b'Open, Call for proposal is open for submission.'), (b'under_review', b'Under review, reviews are being collected prior to board meeting.'), (b'closed', b'Closed, results have been communicated.')]),
            preserve_default=True,
        ),
    ]
