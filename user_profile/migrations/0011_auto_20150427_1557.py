# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0010_auto_20150424_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='zip',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
