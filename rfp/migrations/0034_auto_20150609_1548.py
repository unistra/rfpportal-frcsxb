# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0033_auto_20150609_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='question_1',
            new_name='custom_0',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='question_2',
            new_name='custom_1',
        ),
        migrations.AddField(
            model_name='review',
            name='custom_2',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='custom_3',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='custom_4',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='custom_5',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='custom_6',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='custom_7',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='custom_8',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='custom_9',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
