# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0031_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='confirmation_email_sent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
