# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0006_auto_20150416_1325'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='testsetline',
            unique_together=set([('srno', 'testset'), ('filename', 'testset')]),
        ),
    ]
