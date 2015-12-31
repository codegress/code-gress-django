# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0016_auto_20151231_1320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='samplecase_id',
            new_name='sample',
        ),
        migrations.RenameField(
            model_name='problem',
            old_name='solution_id',
            new_name='sol',
        ),
        migrations.RenameField(
            model_name='samplecase',
            old_name='problem_id',
            new_name='prob',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='problem_id',
            new_name='prob',
        ),
    ]
