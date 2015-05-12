# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0010_testset_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testset',
            name='code',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
