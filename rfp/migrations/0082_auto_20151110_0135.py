# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0081_auto_20151031_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfpcampaign',
            name='budget_eq',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rfpcampaign',
            name='budget_hr',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rfpcampaign',
            name='budget_op',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
