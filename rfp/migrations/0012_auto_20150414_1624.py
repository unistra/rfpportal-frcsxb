# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0011_auto_20150414_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='document',
            field=models.FileField(null=True, upload_to=b'/reviews/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='question_1',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='question_2',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
