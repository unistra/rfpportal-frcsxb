# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0009_auto_20150408_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='document',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
