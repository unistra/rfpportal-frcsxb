# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0056_auto_20150623_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='awarded_amount',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='email_template_review_follow_up',
            field=models.CharField(default=b'review_follow_up_on_invitation_default', max_length=255, null=True, verbose_name='Email template for follow up with reviewer.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rfpcampaign',
            name='email_template_review_invitation',
            field=models.CharField(default=b'review_invitation_email_default', max_length=255, null=True, verbose_name='Email template for invitation to review.', blank=True),
            preserve_default=True,
        ),
    ]
