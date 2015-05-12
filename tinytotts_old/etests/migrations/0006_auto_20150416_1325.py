# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0005_testset_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsetline',
            name='filename',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='testsetline',
            name='srno',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='testsetline',
            unique_together=set([('srno', 'testset')]),
        ),
    ]
