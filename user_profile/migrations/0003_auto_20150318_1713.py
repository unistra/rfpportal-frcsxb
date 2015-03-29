# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_userprofile_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='organization',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='organizationcsdc',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
