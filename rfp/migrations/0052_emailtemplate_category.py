# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0051_auto_20150622_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtemplate',
            name='category',
            field=models.CharField(max_length=255, null=True, choices=[(b'confirmation', b'Email sent when a project is succesfully submitted'), (b'invitation_to_review', b'Email sent to invite a Reviewer to review a specific project')]),
            preserve_default=True,
        ),
    ]
