# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20150617_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='father_name',
            field=models.CharField(default=b'-Not mentioned-', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mother_name',
            field=models.CharField(default=b'-Not mentioned-', max_length=20),
        ),
    ]
