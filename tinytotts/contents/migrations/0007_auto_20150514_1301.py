# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_auto_20150514_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='contenttype',
            field=models.ForeignKey(to='contents.ContentType', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
