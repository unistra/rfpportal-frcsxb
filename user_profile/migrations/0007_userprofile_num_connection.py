# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_userprofile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='num_connection',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
