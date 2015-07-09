# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0063_auto_20150709_1422'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='scope_of_work',
            new_name='abstract',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='purpose',
            new_name='keywords',
        ),
        migrations.RemoveField(
            model_name='project',
            name='anticipated_impact',
        ),
    ]
