# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0021_auto_20160104_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
