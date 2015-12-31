# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0010_auto_20151231_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('statement', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('handle', models.ForeignKey(to='handle.Registration')),
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
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('problem_id', models.ForeignKey(to='handle.Problem')),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='samplecase_id',
            field=models.ForeignKey(to='handle.SampleCase'),
        ),
        migrations.AddField(
            model_name='problem',
            name='solution_id',
            field=models.ForeignKey(to='handle.Solution', null=True),
        ),
    ]
