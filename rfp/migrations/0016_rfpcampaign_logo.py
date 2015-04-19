# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0015_auto_20150417_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfpcampaign',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'image', blank=True),
            preserve_default=True,
        ),
    ]
