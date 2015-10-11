# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phonetics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=100)),
                ('phoneticsname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('groups', models.ManyToManyField(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneticsLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=250, null=True, blank=True)),
                ('srno', models.IntegerField()),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('phonetics', models.ForeignKey(to='base.Phonetics', on_delete=django.db.models.deletion.PROTECT)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='phoneticsline',
            unique_together=set([('srno', 'phonetics')]),
        ),
    ]
