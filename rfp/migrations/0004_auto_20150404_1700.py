# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0003_project_project_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestforproposal',
            name='description',
            field=models.CharField(max_length=4000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rfpcampaign',
            name='instructions',
            field=models.CharField(max_length=4000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='name',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='year',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
    ]
