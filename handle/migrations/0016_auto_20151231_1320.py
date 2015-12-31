# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0015_auto_20151231_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='company',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='country',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='website',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
