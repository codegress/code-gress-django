# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0022_auto_20160104_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
    ]
