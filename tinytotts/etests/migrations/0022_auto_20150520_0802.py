# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0021_auto_20150520_0740'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='testsetline',
            unique_together=set([('srno', 'testset')]),
        ),
    ]
