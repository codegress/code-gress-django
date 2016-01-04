# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0019_auto_20160104_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='sample',
        ),
        migrations.AddField(
            model_name='problem',
            name='sample',
            field=models.ManyToManyField(to='handle.SampleCase', blank=True),
        ),
        migrations.AlterField(
            model_name='samplecase',
            name='time',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='time',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
