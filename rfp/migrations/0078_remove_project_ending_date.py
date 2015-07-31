# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0077_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='ending_date',
        ),
    ]
