# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0049_auto_20150622_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailtemplate',
            old_name='rfp',
            new_name='entity',
        ),
    ]
