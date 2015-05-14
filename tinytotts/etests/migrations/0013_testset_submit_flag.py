# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0012_testset_no_ans'),
    ]

    operations = [
        migrations.AddField(
            model_name='testset',
            name='submit_flag',
            field=models.BooleanField(default=False),
        ),
    ]
