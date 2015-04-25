# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0017_auto_20150420_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=255, null=True, blank=True)),
                ('amount', models.FloatField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='requestforproposal',
            options={'verbose_name': 'Fund', 'verbose_name_plural': 'Funds'},
        ),
        migrations.AlterModelOptions(
            name='rfpcampaign',
            options={'verbose_name': 'Call for proposal', 'verbose_name_plural': 'Call for proposals'},
        ),
    ]
