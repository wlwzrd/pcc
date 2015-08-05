# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=600)),
                ('diagnosis', models.ForeignKey(to='absenteeism.Diagnosis')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('personal_number', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('area', models.ForeignKey(to='absenteeism.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('disease', models.ForeignKey(to='absenteeism.Disease')),
                ('employee', models.ForeignKey(to='absenteeism.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='organization',
            field=models.ForeignKey(to='absenteeism.Organization'),
        ),
    ]
