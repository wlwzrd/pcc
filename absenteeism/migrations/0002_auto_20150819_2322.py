# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('absenteeism', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosisType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=2, choices=[(b'AT', b'Accidente de Trabajo'), (b'EC', b'Enfermedad Cronica')])),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='diagnosis_type',
            field=models.ForeignKey(default=None, to='absenteeism.DiagnosisType', null=True),
        ),
    ]
