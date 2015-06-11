# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0035_remove_review_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfpcampaign',
            name='review_questions',
            field=models.CharField(max_length=4000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='project',
            field=models.ForeignKey(verbose_name='Project', to='rfp.Project', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(verbose_name='Reviewer', to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
    ]
