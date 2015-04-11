# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20150318_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
