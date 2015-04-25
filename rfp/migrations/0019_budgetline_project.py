# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0018_auto_20150424_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetline',
            name='project',
            field=models.OneToOneField(null=True, to='rfp.Project'),
            preserve_default=True,
        ),
    ]
