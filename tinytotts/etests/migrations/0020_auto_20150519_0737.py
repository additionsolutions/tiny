# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0019_auto_20150519_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='testquestion',
            name='preamble',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
