# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0006_auto_20151231_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('correct', models.BooleanField(default=False)),
                ('time', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('answer_id', models.ForeignKey(to='handle.Answer', null=True)),
                ('handle', models.ForeignKey(to='handle.Registration')),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_in', models.TextField()),
                ('test_out', models.TextField()),
                ('time', models.FloatField(null=True, blank=True)),
                ('question_id', models.ForeignKey(to='handle.Question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='testcase_id',
            field=models.ForeignKey(to='handle.TestCase'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(to='handle.Question'),
        ),
    ]
