# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('contents', '0003_remove_contenttype_createdby'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='groups',
            field=models.ManyToManyField(to='auth.Group'),
            preserve_default=True,
        ),
    ]
