# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0047_auto_20150618_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCommunication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('from_email', models.EmailField(max_length=75)),
                ('subject', models.CharField(max_length=255, null=True, blank=True)),
                ('body', models.CharField(max_length=4000, null=True, blank=True)),
                ('rfp', models.ForeignKey(verbose_name='Reviewer', to='rfp.RfpCampaign')),
            ],
            options={
                'ordering': ('from_email',),
            },
            bases=(models.Model,),
        ),
    ]
