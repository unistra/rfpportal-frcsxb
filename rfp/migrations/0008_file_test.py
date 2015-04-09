# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('rfp', '0007_project_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='File_Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('document', models.FileField(null=True, upload_to=django.core.files.storage.FileSystemStorage(location=b'/media/projects/'))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
