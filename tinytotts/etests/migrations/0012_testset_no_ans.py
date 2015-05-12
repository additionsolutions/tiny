# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0011_auto_20150419_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='testset',
            name='no_ans',
            field=models.IntegerField(default=1),
        ),
    ]
