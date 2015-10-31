# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0078_remove_project_ending_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='dropped',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
