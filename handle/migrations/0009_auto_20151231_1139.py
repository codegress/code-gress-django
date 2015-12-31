# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0008_auto_20151231_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SampleCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sample_in', models.TextField()),
                ('sample_out', models.TextField()),
                ('time', models.FloatField(null=True)),
                ('problem_id', models.ForeignKey(to='handle.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('correct', models.BooleanField(default=False)),
                ('time', models.FloatField(null=True)),
                ('problem_id', models.ForeignKey(to='handle.Problem')),
            ],
        ),
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
        migrations.AddField(
            model_name='problem',
            name='case_id',
            field=models.ForeignKey(to='handle.SampleCase'),
        ),
        migrations.AddField(
            model_name='problem',
            name='handle',
            field=models.ForeignKey(to='handle.Registration'),
        ),
        migrations.AddField(
            model_name='problem',
            name='sol_id',
            field=models.ForeignKey(to='handle.Solution', null=True),
        ),
    ]
