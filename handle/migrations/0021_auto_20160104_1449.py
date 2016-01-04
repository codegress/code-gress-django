# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0020_auto_20160104_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
