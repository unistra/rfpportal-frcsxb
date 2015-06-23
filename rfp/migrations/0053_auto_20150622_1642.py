# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0052_emailtemplate_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailtemplate',
            name='rfp',
        ),
        migrations.DeleteModel(
            name='EmailTemplate',
        ),
        migrations.AddField(
            model_name='rfpcampaign',
            name='email_template_project_confirmation',
            field=models.CharField(max_length=255, null=True, verbose_name='Email template for project submission confirmation.', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rfpcampaign',
            name='email_template_review_confirmation',
            field=models.CharField(max_length=255, null=True, verbose_name='Email template for confirmation and thank you for your review.', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rfpcampaign',
            name='email_template_review_follow_up',
            field=models.CharField(max_length=255, null=True, verbose_name='Email template for follow up with reviewer.', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rfpcampaign',
            name='email_template_review_invitation',
            field=models.CharField(max_length=255, null=True, verbose_name='Email template for invitation to review.', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rfpcampaign',
            name='email_template_rfp_closed',
            field=models.CharField(max_length=255, null=True, verbose_name='Email template to anounce results.', blank=True),
            preserve_default=True,
        ),
    ]
