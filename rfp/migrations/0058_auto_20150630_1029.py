# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0057_auto_20150625_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(default=b'pending', max_length=255, choices=[(b'pending', b'Pending'), (b'submitted', b'Submitted'), (b'under_review', b'Under review'), (b'granted', b'Granted'), (b'not_granted', b'Not Granted')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='email_template_project_confirmation',
            field=models.CharField(default=b'project_submission_confirmation_email_default', max_length=255, verbose_name='Email template for project submission confirmation.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='email_template_review_confirmation',
            field=models.CharField(default=b'review_submission_confirmation_email_default', max_length=255, verbose_name='Email template for confirmation and thank you for your review.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='email_template_review_follow_up',
            field=models.CharField(default=b'review_follow_up_on_invitation_default', max_length=255, verbose_name='Email template for follow up with reviewer.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='email_template_review_invitation',
            field=models.CharField(default=b'review_invitation_email_default', max_length=255, verbose_name='Email template for invitation to review.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='email_template_rfp_closed',
            field=models.CharField(default=b'project_results_anouncement_email_default', max_length=255, verbose_name='Email template to anounce results.'),
            preserve_default=True,
        ),
    ]
