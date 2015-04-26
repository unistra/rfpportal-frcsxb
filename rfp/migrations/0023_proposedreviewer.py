# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0022_auto_20150425_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposedReviewer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255, null=True, blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('institution', models.CharField(max_length=255, null=True, blank=True)),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
                ('city', models.CharField(max_length=255, null=True, blank=True)),
                ('state', models.CharField(max_length=255, null=True, blank=True)),
                ('postcode', models.IntegerField(null=True, blank=True)),
                ('country', models.CharField(max_length=255, null=True, blank=True)),
                ('project', models.ForeignKey(to='rfp.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
