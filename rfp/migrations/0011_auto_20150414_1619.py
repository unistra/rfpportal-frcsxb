# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0010_auto_20150408_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='document',
            field=models.FileField(null=True, upload_to=b'/reviews/'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='question_1',
            field=models.CharField(max_length=4000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='question_2',
            field=models.CharField(max_length=4000, null=True),
            preserve_default=True,
        ),
    ]
