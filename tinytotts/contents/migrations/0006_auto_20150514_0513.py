# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_auto_20150514_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='enddate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='content',
            name='startdate',
            field=models.DateField(),
        ),
    ]
