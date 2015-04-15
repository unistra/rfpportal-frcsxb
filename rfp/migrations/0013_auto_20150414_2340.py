# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0012_auto_20150414_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='ending_date',
        ),
        migrations.AlterField(
            model_name='project',
            name='anticipated_impact',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='document',
            field=models.FileField(null=True, upload_to=b'projects', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='project_duration',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='purpose',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='scope_of_work',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='document',
            field=models.FileField(null=True, upload_to=b'reviews', blank=True),
            preserve_default=True,
        ),
    ]
