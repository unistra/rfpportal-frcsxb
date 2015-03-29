# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20150318_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='organizationcsdc',
            new_name='organization',
        ),
    ]
