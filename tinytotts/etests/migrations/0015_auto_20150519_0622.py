# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0014_auto_20150519_0545'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preamble', models.CharField(max_length=200)),
                ('question', models.CharField(max_length=500)),
                ('duration', models.IntegerField()),
                ('image', models.URLField()),
                ('category', models.ForeignKey(to='etests.Category', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
        migrations.AddField(
            model_name='option',
            name='mark',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='option',
            name='question',
            field=models.ForeignKey(to='etests.TestQuestion', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
