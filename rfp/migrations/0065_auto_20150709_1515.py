# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0064_auto_20150709_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfpcampaign',
            name='project_questions',
            field=models.TextField(max_length=4000, null=True, verbose_name='Project questions (one question per line, maximum of 10 questions permitted.)', blank=True),
            preserve_default=True,
        ),
    ]
