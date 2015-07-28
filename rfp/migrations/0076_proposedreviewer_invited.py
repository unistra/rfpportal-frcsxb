# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0075_auto_20150724_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposedreviewer',
            name='invited',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
