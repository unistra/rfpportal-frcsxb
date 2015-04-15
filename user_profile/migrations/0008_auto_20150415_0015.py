# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_userprofile_num_connection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='num_connection',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=True,
        ),
    ]
