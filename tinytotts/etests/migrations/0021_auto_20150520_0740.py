# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0020_auto_20150519_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='option',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
