# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0006_auto_20150404_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='document',
            field=models.FileField(null=True, upload_to=django.core.files.storage.FileSystemStorage(location=b'/media/projects/')),
            preserve_default=True,
        ),
    ]
