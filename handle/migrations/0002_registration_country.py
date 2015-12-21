# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='country',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
