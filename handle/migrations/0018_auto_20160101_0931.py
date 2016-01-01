# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0017_auto_20151231_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='full_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
