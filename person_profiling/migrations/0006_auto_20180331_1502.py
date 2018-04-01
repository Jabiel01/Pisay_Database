# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-31 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_profiling', '0005_auto_20180331_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='club',
            field=models.CharField(choices=[('1', 'ICONS'), ('2', 'SCI-WINGS')], default=None, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='club',
            field=models.CharField(choices=[('1', 'ICONS'), ('2', 'SCI-WINGS')], default=None, max_length=13, null=True),
        ),
    ]