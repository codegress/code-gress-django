# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0018_auto_20160101_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='sample',
            field=models.ForeignKey(blank=True, to='handle.SampleCase', null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='sample_in_desc',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='sample_out_desc',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='sol',
            field=models.ForeignKey(blank=True, to='handle.Solution', null=True),
        ),
    ]
