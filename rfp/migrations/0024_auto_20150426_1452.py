# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0023_proposedreviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposedreviewer',
            name='project',
            field=models.ForeignKey(to='rfp.Project', null=True),
            preserve_default=True,
        ),
    ]
