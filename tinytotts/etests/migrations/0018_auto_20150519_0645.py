# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0017_auto_20150519_0633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='image',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='testquestion',
            old_name='image',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='option',
            name='mark',
            field=models.IntegerField(),
        ),
    ]
