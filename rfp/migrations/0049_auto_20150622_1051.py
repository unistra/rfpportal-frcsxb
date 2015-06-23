# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0048_emailcommunication'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmailCommunication',
            new_name='EmailTemplate',
        ),
    ]
