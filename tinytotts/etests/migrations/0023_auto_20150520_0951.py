# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0022_auto_20150520_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='SrNo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='option',
            unique_together=set([('t_question', 'SrNo')]),
        ),
    ]
