# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0060_auto_20150702_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfpcampaign',
            name='starting_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 8, 20, 23, 48, 754000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='project_questions',
            field=models.TextField(default=b'Abstract/r/n', max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
