# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_contenttype_createdby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contenttype',
            name='createdby',
        ),
    ]
