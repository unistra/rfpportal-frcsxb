# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0019_budgetline_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ending_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
