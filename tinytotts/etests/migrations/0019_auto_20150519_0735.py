# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0018_auto_20150519_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testquestion',
            name='duration',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='testquestion',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
