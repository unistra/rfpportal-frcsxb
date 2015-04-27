# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0025_budgetline_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetline',
            name='category',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='budgetline',
            name='project',
            field=models.ForeignKey(editable=False, to='rfp.Project', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proposedreviewer',
            name='postcode',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
