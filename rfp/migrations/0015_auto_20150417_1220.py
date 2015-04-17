# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0014_auto_20150417_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='document',
            field=models.FileField(null=True, upload_to=b'project', blank=True),
            preserve_default=True,
        ),
    ]
