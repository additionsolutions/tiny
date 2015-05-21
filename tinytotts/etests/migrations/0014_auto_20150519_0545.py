# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('etests', '0013_testset_submit_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option', models.CharField(max_length=200)),
                ('SrNo', models.CharField(unique=True, max_length=100)),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preamble', models.CharField(max_length=200)),
                ('question', models.CharField(max_length=500)),
                ('mark', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('image', models.URLField()),
                ('category', models.ForeignKey(to='etests.Category', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='etests.TestSetLine', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='testsetline',
            name='testset',
            field=models.ForeignKey(to='etests.TestSet', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(to='etests.Question'),
        ),
    ]
