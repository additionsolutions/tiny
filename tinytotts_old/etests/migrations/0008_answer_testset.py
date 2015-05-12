# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0007_auto_20150416_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='testset',
            field=models.ForeignKey(default=1, to='etests.TestSet'),
            preserve_default=False,
        ),
    ]
