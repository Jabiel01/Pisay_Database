# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-31 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_profiling', '0007_auto_20180331_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='balance',
            field=models.IntegerField(blank=0, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]