# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0042_rfpcampaign_add_reviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 16, 0, 21, 34, 200000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
