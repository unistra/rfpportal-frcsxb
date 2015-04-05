# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0004_auto_20150404_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfpcampaign',
            name='request_for_proposal',
            field=models.ForeignKey(default=1, to='rfp.RequestForProposal'),
            preserve_default=False,
        ),
    ]
