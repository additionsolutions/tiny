# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0008_answer_testset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='testset',
        ),
    ]
