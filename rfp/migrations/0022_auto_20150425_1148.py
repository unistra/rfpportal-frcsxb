# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0021_project_additional_funding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='additional_funding',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='purpose',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
