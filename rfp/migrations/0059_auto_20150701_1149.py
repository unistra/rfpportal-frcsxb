# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0058_auto_20150630_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfpcampaign',
            name='project_questions',
            field=models.TextField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='review_questions',
            field=models.TextField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
