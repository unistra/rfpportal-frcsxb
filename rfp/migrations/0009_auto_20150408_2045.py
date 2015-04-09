# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0008_file_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_test',
            name='document',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
