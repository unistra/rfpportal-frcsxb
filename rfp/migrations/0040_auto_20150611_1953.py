# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0039_review_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='anticipated_impact',
            field=models.CharField(max_length=4000, null=True, verbose_name='Link with other project', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='scope_of_work',
            field=models.CharField(max_length=4000, null=True, verbose_name='Abstract', blank=True),
            preserve_default=True,
        ),
    ]
