# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0061_auto_20150708_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default=b'pending', max_length=255, choices=[(b'draft', b'Draft'), (b'submitted', b'Submitted'), (b'under_review', b'Under review'), (b'granted', b'Granted'), (b'not_granted', b'Not Granted')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='project_questions',
            field=models.TextField(default=b'Abstract', max_length=4000, null=True, verbose_name='Project questions (one question per line, maximum of 10 questions permitted.)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='review_questions',
            field=models.TextField(max_length=4000, null=True, verbose_name='Review questions (one question per line, maximum of 10 questions permitted.)', blank=True),
            preserve_default=True,
        ),
    ]
