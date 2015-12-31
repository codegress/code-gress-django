# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0003_auto_20151231_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_id',
            field=models.ForeignKey(to='handle.Answer', blank=True),
        ),
    ]
