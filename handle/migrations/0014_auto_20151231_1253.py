# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0013_auto_20151231_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
