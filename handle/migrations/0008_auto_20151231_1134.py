# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0007_auto_20151231_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcase',
            old_name='test_in',
            new_name='sample_in',
        ),
        migrations.RenameField(
            model_name='testcase',
            old_name='test_out',
            new_name='sample_out',
        ),
    ]
