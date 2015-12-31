# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0005_auto_20151231_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question_id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='handle',
        ),
        migrations.RemoveField(
            model_name='question',
            name='testcase_id',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='question_id',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='TestCase',
        ),
    ]
