# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_content_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='enddate',
            field=models.DateField(default=datetime.datetime(2015, 5, 14, 5, 4, 58, 948345)),
        ),
        migrations.AddField(
            model_name='content',
            name='startdate',
            field=models.DateField(default=datetime.datetime(2015, 5, 14, 5, 4, 58, 948262)),
        ),
    ]
