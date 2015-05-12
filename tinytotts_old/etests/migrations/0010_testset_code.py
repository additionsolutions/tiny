# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0009_remove_answer_testset'),
    ]

    operations = [
        migrations.AddField(
            model_name='testset',
            name='code',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
