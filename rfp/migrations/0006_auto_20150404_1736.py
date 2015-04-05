# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0005_rfpcampaign_request_for_proposal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforproposal',
            name='description',
            field=models.TextField(max_length=4000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='instructions',
            field=models.TextField(max_length=4000, null=True),
            preserve_default=True,
        ),
    ]
