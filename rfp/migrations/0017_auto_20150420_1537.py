# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0016_rfpcampaign_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='project',
            field=models.ForeignKey(verbose_name='Project', to='rfp.Project'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(verbose_name='Reviewer', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
