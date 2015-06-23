# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0050_auto_20150622_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailtemplate',
            name='entity',
        ),
        migrations.AddField(
            model_name='emailtemplate',
            name='rfp',
            field=models.ForeignKey(verbose_name='Request for Proposal', to='rfp.RfpCampaign', null=True),
            preserve_default=True,
        ),
    ]
