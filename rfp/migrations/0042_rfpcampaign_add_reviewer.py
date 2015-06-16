# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0041_auto_20150614_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfpcampaign',
            name='add_reviewer',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
