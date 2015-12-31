# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0009_auto_20151231_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='case_id',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='handle',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='sol_id',
        ),
        migrations.RemoveField(
            model_name='samplecase',
            name='problem_id',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='problem_id',
        ),
        migrations.DeleteModel(
            name='Problem',
        ),
        migrations.DeleteModel(
            name='SampleCase',
        ),
        migrations.DeleteModel(
            name='Solution',
        ),
    ]
