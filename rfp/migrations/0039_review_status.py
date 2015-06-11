# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0038_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.CharField(default=b'pending', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
