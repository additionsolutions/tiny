# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0016_auto_20150519_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='testsetline',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='etests.TestQuestion', null=True),
        ),
        migrations.AlterField(
            model_name='testsetline',
            name='filename',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
