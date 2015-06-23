# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0053_auto_20150622_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfpcampaign',
            name='email_template_project_confirmation',
            field=models.CharField(default=b'project_submission_confirmation_email_default', max_length=255, null=True, verbose_name='Email template for project submission confirmation.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='email_template_review_confirmation',
            field=models.CharField(default=b'review_submission_confirmation_email_default', max_length=255, null=True, verbose_name='Email template for confirmation and thank you for your review.', blank=True),
            preserve_default=True,
        ),
    ]
