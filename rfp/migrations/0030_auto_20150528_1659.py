# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0029_review_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='type',
        ),
        migrations.AddField(
            model_name='proposedreviewer',
            name='type',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
