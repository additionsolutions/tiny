# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0015_auto_20150519_0622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='question',
            new_name='t_question',
        ),
        migrations.RenameField(
            model_name='testquestion',
            old_name='question',
            new_name='test_question',
        ),
    ]
