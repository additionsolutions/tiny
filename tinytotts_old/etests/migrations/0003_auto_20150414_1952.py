# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0002_testsetline_srno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsetline',
            name='srno',
            field=models.IntegerField(unique=True),
        ),
    ]
