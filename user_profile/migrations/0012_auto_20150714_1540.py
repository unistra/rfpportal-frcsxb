# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0011_auto_20150427_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='num_rated_review',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rated_review_avg',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=True,
        ),
    ]
