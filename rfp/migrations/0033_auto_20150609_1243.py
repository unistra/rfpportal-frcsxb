# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0032_project_confirmation_email_sent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rfpcampaign',
            name='request_for_proposal',
        ),
        migrations.DeleteModel(
            name='RequestForProposal',
        ),
    ]
