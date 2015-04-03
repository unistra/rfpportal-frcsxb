# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='anticipated_impact',
            field=models.CharField(max_length=4000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='ending_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='purpose',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='requested_amount',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='scope_of_work',
            field=models.CharField(max_length=4000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='starting_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
