# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0012_auto_20151231_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='last_name',
        ),
        migrations.AddField(
            model_name='registration',
            name='company',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
