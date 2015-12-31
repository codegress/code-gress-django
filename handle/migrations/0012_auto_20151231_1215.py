# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0011_auto_20151231_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='note',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='sample_in_desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='sample_out_desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='website',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
