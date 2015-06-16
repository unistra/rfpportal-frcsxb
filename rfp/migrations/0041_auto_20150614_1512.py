# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0040_auto_20150611_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfpcampaign',
            name='category',
            field=models.CharField(max_length=255, null=True, choices=[(b'Synergy', b'Synergy'), (b'Innovation', b'Innovation'), (b'Labex_CSC', b'Labex CSC')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='purpose',
            field=models.CharField(max_length=4000, null=True, verbose_name='Keywords', blank=True),
            preserve_default=True,
        ),
    ]
