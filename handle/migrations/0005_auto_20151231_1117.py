# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0004_auto_20151231_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_id',
            field=models.ForeignKey(to='handle.Answer', null=True),
        ),
    ]
