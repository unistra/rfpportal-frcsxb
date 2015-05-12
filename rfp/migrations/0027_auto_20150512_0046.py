# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0026_auto_20150427_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetline',
            name='duration',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='budgetline',
            name='monthly_salary',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='budgetline',
            name='quote',
            field=models.FileField(null=True, upload_to=b'quote', blank=True),
            preserve_default=True,
        ),
    ]
